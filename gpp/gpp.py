#!/bin/python3

import re
import os
import sys
import argparse
import itertools
from typing import List, Dict
from datetime import datetime

def write_file(name: str, content: str) -> None:
    out_file = open(name, "w")
    out_file.write(content)
    out_file.close()


def init_defs() -> Dict[str, str]:
    defines: Dict[str, str] = dict()
    defines['__FILE__'] = os.getcwd()
    defines['__DATE__'] = datetime.today().strftime('%Y-%m-%d')
    defines['__TIME__'] = datetime.today().strftime('%H:%M:%S')

    return defines


def read_file(file_name: str) -> str:
    lines: List[str] = list()
    with open(file_name, encoding='utf-8') as file_in:
        for line in file_in:
            lines.append(line)

    return lines


def handle_logical_ops(arg1: str, arg2: str, op: str) -> bool:

    if arg1 in defines.keys():
        arg1 = defines[arg1]

    if arg2 in defines.keys():
        arg2 = defines[arg2]

    if op == '>':
        return arg1 > arg2
    if op == '<':
        return arg1 < arg2
    if op == '==':
        return arg1 == arg2
    if op == '>=':
        return arg1 >= arg2
    if op == '<=':
        return arg1 <= arg2
    if op == '!=':
        return arg1 != arg2
    if op == 'or':
        return arg1 or arg2
    if op == 'and':
        return arg1 and arg2
    if op == 'nand':
        return arg1 and not arg2


def apply_defs(inp: str, defs: Dict[str, str]) -> str:
    for key, value in defines.items():
        inp = inp.replace(key, value)

    return inp


def handle_include(inp: str) -> List[str]:
    return ['\n'.join(read_file(inp.split()[1].lstrip('"').strip('"')))]


def handle_if(inp: str) -> List[str]:
    temp: List[str] = []
    i: int = 0
    type_: str = ''

    while i < len(inp):

        keywords = inp[i].split(' ')
        condition: bool = False

        if keywords[0] == '#if':
            type_ = 'if'
        elif keywords[0] == '#ifdef':
            type_ = 'def'
        elif keywords[0] == '#ifndef':
            type_ = 'ndef'

        if type_ == 'if':
            condition = handle_logical_ops(keywords[1], keywords[3], keywords[2])

        if type_ == 'def':
            condition = defines.get(keywords[1], False)

        if type_ == 'ndef':
            condition = not defines.get(keywords[1], False)

        if condition:

            while True:

                if inp[i].strip().startswith('#endif'):
                    return temp[:-1]

                if inp[i].strip().startswith('#else'):

                    while True:

                        if inp[i].strip().startswith('#endif'):
                            return temp[1:-1]

                        i += 1

                i += 1
                temp.append(inp[i])

        else:
            while True:

                if inp[i].strip().startswith('#else'):
                    break

                if inp[i].strip().startswith('#endif'):
                    return temp

                i += 1

            while True:

                if inp[i].strip().startswith('#endif'):
                    return temp[:-1]

                if inp[i].strip().startswith('#else'):

                    while True:
                        i += 1

                        temp.append(inp[i])
                        if inp[i].strip().startswith('#endif'):
                            return temp[:-1]

                i += 1


def handle_define(inp: str) -> None:
    keywords = inp.strip().split()

    defines[keywords[1]] = ''.join(keywords[2:])


def handle_undef(inp: str) -> None:
    keywords = inp.strip().split()

    del defines[keywords[1]]


def stringify(s: List[str]) -> str:
    s = '\n'.join(list(itertools.chain(*s)))  # flatten: [[[]], [], []] -> [[], [], [] ...]
    return re.sub('[\n]+', '\n', s)  # remove multiple white spaces from the str


def if_expression(inp: str) -> (List[str], int):
    jump: int = 0
    res: List[str] = handle_if(inp)

    while True:

        if inp[jump].strip().startswith('#endif'):
            jump += 1  # 1 is added to skip the '#endif'
            break

        jump += 1

    return res, jump


def handle_exp(inp: str):
    temp = []
    i: int = 0
    inp = inp.split('\n')

    while i < len(inp):

        if inp[i].strip().startswith('#include'):
            res = handle_include(inp[i])
            i += 1
            temp.append(res)

        if inp[i].strip().startswith('#define'):
            handle_define(inp[i])
            i += 1

        if inp[i].strip().startswith('#undef'):
            handle_undef(inp[i])
            i += 1

        if inp[i].strip().startswith('#if'):
            res, jump = if_expression(inp[i:])
            i += jump
            temp.append(res)

        else:
            temp.append([inp[i]])
            i += 1

    return temp


if __name__ == '__main__':
    defines = init_defs()

    parser = argparse.ArgumentParser(description='Args for GPP')

    parser.add_argument('-E', action='store_true', help='print the pre-processor output to the console')
    parser.add_argument('file', help='relative path to the input file')
    parser.add_argument('-o', help='relative path to the output file', default='gpp.out')
    parser.add_argument('--run', help='relative path to the input file', nargs='+')

    options = parser.parse_args()
    out_file = options.o

    if not options.file:
        print(f"[ERROR] you must provide a path")
        sys.exit()

    if not os.path.exists(options.file):
        print(f"[ERROR] path: {str(options.file)} does not exist")
        sys.exit()

    inp = read_file(options.file)
    inp = '\n'.join(inp)

    out = handle_exp(inp)
    out = stringify(out)
    out = apply_defs(out, defines)

    write_file(options.o, out)

    if options.E:
        print("[INFO] logging the pre-processer output", end='\n\n')
        print(out, end='')

    if options.run:
        os.system(' '.join(options.run))
