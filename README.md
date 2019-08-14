# 🌲 Forest 🌲

A Python-based, forest-themed programming language. Coming soon!

# 🐻 [![Build Status](https://travis-ci.org/lucianmot/f.rest.svg?branch=master)](https://travis-ci.org/lucianmot/f.rest)

## How to Install

* Ensure you have Python v3.7.4 installed.
* Clone this repository.
* Install code coverage tool:

```console
$ pip3 install coverage
```

### Test and Code Coverage (via Script)

A script is included to run all tests and code coverage (recommended).

```console
$ bash test_script
```

Read the output on the console, and open the htmlcov/index.html file to view details of coverage.

## How to Test (Manually)

run the command below specifiying the test file to be included.

```console
$ python3 -m unittest interpreter_test.py
```

## How to Check Code Coverage (Maually)

Run the code coverage report:

```console
$ coverage interpreter_test.py
$ coverage html
```

## How to Run

In the pis (interactive shell) use command python3 to initiate.

Commands:
```console
$ python3
```
```python
>>> from forest import Interpreter
>>> interpreter = Interpreter("echo<<Hello World!>>")
>>> interpreter.response()
>>> 'Forest says: Hello World!'
```

Try putting your own message between the `<<tree tops>>`!   

**Variable assignment**  

```
BACKPACK:myvar^PACK_WITH^<<bears 🐻🐻🐻>> 

// echo^myvar should print 'bears 🐻🐻🐻'
```

Take care, don't start the fire.


## Design

The diagram below shows how our interpreter is built:

![interpreter](Interpreterv2.jpg)
