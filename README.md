# 🌲 Forest language 🌲

A Python-based, forest-themed programming language. Coming soon!

# 🐻

## How to Install

* Ensure you have Python v3.7.4 installed.
* Clone this repository.

## How to Test

```console
$ python3 -m unittest echo_test.py tokeniser_test.py
```

## How to Check Code Coverage

Install code coverage tool:

```console
$ pip3 install coverage
```
Run the code coverage report:

```console
$ coverage run forest.py echo_test.py tokeniser_test.py
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
```
Take care, don't start the fire. 

## Design

The diagram below shows how our interpreter is built:

![interpreter](Interpreterv2.jpg)