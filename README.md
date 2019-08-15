# 🌲 Forest language 🌲

A Python-based, forest-themed programming language. Now in Alpha!

# 🐻 [![Build Status](https://travis-ci.org/lucianmot/f.rest.svg?branch=master)](https://travis-ci.org/lucianmot/f.rest)

## Team:
| | | | | |
| --- | --- | --- | --- | --- |  
| ![](github.png) [Aleks](https://github.com/ajmpawlik) | ![](github.png) [Anna](https://github.com/aniasobo) | ![](github.png) [James](https://github.com/zepherine2006DEV) | ![](github.png) [Joe](https://github.com/josephtownshend) | ![](github.png) [Lucian](https://github.com/lucianmot) |    

[Forest website](https://forest-code.herokuapp.com/)  

---
## How to Install Forest

* Ensure you have Python v3.7.4 installed.
* Clone or download this repository.

### Run Forest as a shell script

`$ python3 forest.py` will open a little Forest REPL. You should see a `=❱❯❭>` tree in your command line prompt. 


## Test and Code Coverage (via Script)

Install code coverage tool:

```console
$ pip3 install coverage
```

We've included a script to run all tests and code coverage (recommended):

```console
$ bash test_script
```

Read the output on the console, and open the htmlcov/index.html file to view details of coverage.

### How to Test (Manually)

run the command below specifiying the test file to be included.

```console
$ python3 -m unittest interpreter_test.py
```

### How to Check Code Coverage (Maually)

Run the code coverage report:

```console
$ coverage interpreter_test.py
$ coverage html
```
---
## Using Forest

### At the moment, Forest has the following capabilities:
* echo any text within `<<tree tops>>` with `echo<<this message>>`
* use the owl operators for comparison of integers: `4^OvO^5` should return `false`; `5^XvX^6` should return `true`    
* use the crow operator to calculate modulus of integers: `9^(*)>^2` should return ` 1`  
* if statement: start your if statement with `WALK_PATH_IF_SEE` and end with `CAMP`  
* TODO: create variables `BACKPACK:myvar^PACK_WITH^<<some text>>`
* use `^` trees between operators and expressions (as you would with spaces in most programming languages) to avoid errors  
* but if you do end up with errors, we've added lots of unhelpful but entertaining bears to the error messages 🐻

### FizzBuzz in Forest! 

```
$ WALK_PATH_IF_SEE^30^(*)>^15^OvO^0^echo^<<fizzbuzz>>^  
$ WALK_PATH_IF_SEE^6^(*)>^3^OvO^0^echo^<<fizz>>^  
$ WALK_PATH_IF_SEE^10^(*)>^5^OvO^0^echo^<<buzz>>^CAMP
```

### Reference:

| Forest | Forest explicit | Human |   
| --- | --- | --- |   
| <<>> | shovels/tree tops | string delimiters |  
| ^ | tree operator | space/general delimiter |  
| OvO | Owl operator | == equals/comparison |  
| XvX | Dead owl operator | != not equal |    
| (*)> | Crow operator | % modulo |   
| ^._.^ | Bat operator | (sadly unused but LOOK HOW COOL IT IS! TODO for version 2.0) |      
| WALK_PATH_IF_SEE | do this if | if statement start |  
| BACKPACK: | create backpack | variable instantiation |   
| PACK_WITH | store in backpack | = variable assignment |  
| CAMP | end statement | end of expression |  
| true/false | acceptable booleans |  


## Design

The diagram below shows how our interpreter is built:

![interpreter](Interpreterv2.jpg)


Take care, and don't start a fire. ʕ•ᴥ•ʔﾉ♡
