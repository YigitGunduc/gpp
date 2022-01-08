<div align="center">
  <h3 align="center">GPP</h1>

  <h3 align="center">General Porpuse Pre-processor</h1>
  
  <p align="center">
  </p>
</div>
<br />


Use C like Pre-Processor directives with any language(Python, Javascript, Shell,
even text documents). A project to bring Pre-processor directives to everywhere

<!-- GETTING STARTED -->
## Getting Started


### Installing
Install the gpp with the folloning script

Using curl
```sh
curl https://raw.githubusercontent.com/yigitgunduc/gpp/master/scripts/install.sh > install.sh && bash install.sh
```

Using wget
```sh
wget https://raw.githubusercontent.com/yigitgunduc/gpp/master/scripts/install.sh && bash install.sh
```

* tools for building the project and installing it will be present in the 
```script/```

### CLI Interface

| flag        | description                                            |
|-------------|--------------------------------------------------------|
| ```-o```    | name of the output file                                |
| ```-E```    | outputs the result of the preprocessor to the terminal |
| ```file```  | name of the input file                                 |
| ```--run``` | command to execute after done processing the file      |

running the pre-processor and generating an output file
```bash
gpp filename -o output
```

running the pre-processor and printing the results to the terminal
```bash
gpp filename -E
```

running the pre-processor and executing a command
```bash
gpp filename -o myproject.sh --run "bash myproject.sh"
```


### Syntax Basics

| Keyword        | description | example
|----------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ```#include``` | include contents of other files to the current one                   | ```#include "hey.sh"```                                                                                                          |
| ```#define```  | Define pre-processor directives that will be replaced before runtime | <pre>#define MY_DEF 10<br>#define HEY 'hey'<br>#define IS_DEF</pre>                                                  |
| ```#undef```   | Undefine defined pre-processor directives                            | ```#undef MY_DEF```                                                                                                              |
| ```#if```      | Compare number, defines, string                                      | <pre>#define MY_DEF 10<br><br>#if MY_DEF == 10<br>  echo "its equal"<br>#endif<br></pre>                                     |
| ```#else```    | Else branch for if statments                                         | <pre>#define MY_DEF 10<br><br>#if MY_DEF != 10<br>  echo "its equal"<br>#else<br>  echo "not equal"<br>#endif<br><br></pre>  |
| ```#ifdef```   | check if a macro have been defined                                   | <pre>#define DEF<br>#ifdef DEF<br>    echo "defined"<br>#endif<pre>                                              |
| ```#ifndef```  | check if a macro have not been defined                               | <pre>#define DEF<br><br><br>#ifndef DEF<br>    echo "not defined"<br>#endif<pre>                                 |

* various example with different programming languages can be found in the 
```example/``` dir

## Syntax Guidlines
* There shoul not be any space between ```#``` and the keyword(define, if, ifdef, include, ...)
* All if expression must be trailed with end ```#endif```

### Examples

- including contents of a file to an other one
```bash
#include "hey.sh"
```

- define a macro
```bash
#define MY_MACRO 5
```

- __FILE__ macro
```bash
echo __FILE__
```
will be replaced the cwd 

- __TIME__ macro
```bash
echo __TIME__
```
will be replaced the time in the HH:MM:SS format

- __DATE__ macro
```bash
echo __DATE__
```
will be replaced the date in the YYYY-MM-DD format

- undefine a macro
```bash
#define MY_MACRO 5

#undef MY_MARCO
```

- comparint two number with an if statement
```bash
#if 4 == 4
  echo "equal"
#endif
```

- comparint macros with an if statement
```bash
#define MY_MACRO 5

#if MY_MACRO == 5
  echo "equal"
#endif
```

- else branch for if statements
```bash
#define MY_MACRO 5

#if MY_MACRO == 3
  echo "equal to 3"
#else
  echo "equal to something else"
#endif
```

- check if a macro is defined
```bash
#define MY_MACRO

#ifdef MY_MACRO
  echo "it's defined"
#else
  echo "not defined"
#endif
```

- check if a macro is not defined
```bash
#define MY_MACRO

#ifndef MY_MACRO  
  echo "not defined"
#else
  echo "it's defined"
#endif
```

- all the keywords together
```bash
#include "hey.sh"

#define AREA 43

#define W 43

#if W == AREA
  echo "equal"
#else
  echo "not equal"
#endif

#ifdef MACRO
  echo "not defined"
#else
  echo "it's defined"
#endif

echo "you are working in the __FILE__ dir"
echo "time is __TIME__"
echo "todays date is __DATE__"

echo "it's done"
```

* various example with different programming languages can be found in the 
```example/``` dir

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/yigitgunduc/gpp/issues) for a full list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
