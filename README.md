<h1 align="center">GPP</h1>

<h1 align="center">General Porpuse Pre-processor</h1>

Use C like Pre-Processor directives with any language(Python, Javascript, Shell,
even text documents). A project to bring Pre-processor directives to everywhere

## Installing
Install the gpp with the folloning script

Using curl
```sh
curl https://raw.githubusercontent.com/user/yigitgunduc/gpp/master/scripts/install.sh && bash install.sh
```

Using wget
```sh
wget https://raw.githubusercontent.com/user/yigitgunduc/gpp/master/scripts/install.sh && bash install.sh
```

## Quick Start
running you project
```bash
gpp -f filename -o output
```

## Syntax Basics

### #include 

include contents of other files to the current one
```bash
#include "hey.sh"
```

### #define

Define pre-processor directives that will be replaced before runtime

```bash
#define MY_DEF 10
#define HEY 'hey'
#define IS_DEF
```

### #undef
Undefine defined pre-processor directives
```bash
#define MY_DEF 10

#undef MY_DEF
```

### #if 
Compare number, defines, string
  
```bash
#define MY_DEF 10

#if MY_DEF == 10
  echo "its equal"
#endif
```

### #else

Else branch for if statments
```bash
#define MY_DEF 10

#if MY_DEF != 10
  echo "its equal"
#else
  echo "not equal"
#endif
```

### #ifdef
### #ifndef

> for more info and examples please see the ```docs/```

## Project structure

```
.
├── docs
├── examples
│   ├── python
│   │   ├── hey.py
│   │   ├── if_else_exp.py
│   │   ├── if_exp.py
│   │   └── include_exp.py
│   └── shell
│       ├── hey.sh
│       ├── if_else_exp.sh
│       ├── if_exp.sh
│       └── include_exp.sh
├── LICENSE
├── README.md
├── scripts
│   ├── build.sh
│   └── install.sh
└── src
    ├── gpp.py
    ├── hey.sh
    └── test.sh
```

* various example with different programming languages can be found in the 
```example/``` dir
* tools like building the project and installing will be present in the 
```script/```
