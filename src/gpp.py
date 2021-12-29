#!/bin/python3

import re
import itertools
from typing import List, Dict

defines: Dict[str, str] = dict()


def read_file(file_name: str) -> List[str]:
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


def apply_defs(inp: str) -> str:
    for key, value in defines.items():
        inp = inp.replace(key, value)

    return inp


def handle_include(inp: str) -> List[str]:
    return ['\n'.join(read_file(inp.split()[1].lstrip('"').strip('"')))]


def handle_if(inp: str) -> List[str]:
    temp: List[str] = []
    i: int = 0

    while i < len(inp):

        keywords = inp[i].split(' ')
        if handle_logical_ops(keywords[1], keywords[3], keywords[2]):

            while True:

                if inp[i].strip().startswith('#endif'):
                    return temp[:-1]

                if inp[i].strip().startswith('#else'):

                    while True:

                        if inp[i].strip().startswith('#endif'):
                            return temp[1:]

                        i += 1

                temp.append(inp[i])
                i += 1

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


def prep(inp: str):
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

    test = '''
#include "hey.sh"

#define AREA 43

#define W 43

#if W == AREA
    echo equal
    echo equal
#else
    echo not equal
    echo not equal again
#endif
print(hey)
echo "HEY"
    '''

    test1 = '\n'.join(read_file('./test.sh'))

    print('output')
    print('======================================')
    print()

    a = prep(test)

    print()
    # print(a)
    print()
    print(apply_defs(stringify(a)))
