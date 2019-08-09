import unittest
from forest import Interpreter

class TestInterpreter(unittest.TestCase):

    def test_intepreter_should_be_initialized_with_text(self):
        interpreter = Interpreter("echo")
        self.assertEqual(interpreter.text, "echo")

    def test_interpreter_should_return_e_when_user_enters_e(self):
        interpreter = Interpreter("echo<<e>>")
        self.assertEqual(interpreter.response(), "e")

    def test_interpreter_should_return_A_when_user_enters_A(self):
        interpreter = Interpreter("echo<<A>>")
        self.assertEqual(interpreter.response(), "A")

    def test_interpreter_should_return_Exception_when_user_enters_4(self):
        interpreter = Interpreter("echo<<4>>")
        self.assertEqual(interpreter.response(), "4")

    def test_interpreter_should_return_Hello_World(self):
        interpreter = Interpreter("echo<<Hello World!>>")
        self.assertEqual(interpreter.response(), "Hello World!")

from forest import Tokeniser

class TestTokeniser(unittest.TestCase):

    def test_method_returns_string_token_when_passed_e(self):
        tokeniser = Tokeniser("echo<<e>>")
        self.assertEqual(tokeniser.create_token(), {"ECHO" : "echo", "STRSTART" : "<<", "STRING" : "e", "STRSTOP" : ">>"})

    def test_method_returns_string_token_when_passed_a(self):
        tokeniser = Tokeniser("echo<<a>>")
        self.assertEqual(tokeniser.create_token(), {"ECHO" : "echo", "STRSTART" : "<<", "STRING" : "a", "STRSTOP" : ">>"})

    def test_method_returns_string_token_when_passed_caps_z(self):
        tokeniser = Tokeniser("echo<<Z>>")
        self.assertEqual(tokeniser.create_token(), {"ECHO" : "echo", "STRSTART" : "<<", "STRING" : "Z", "STRSTOP" : ">>"})

    def test_method_returns_exception_when_passed_number(self):
        tokeniser = Tokeniser("9")
        self.assertRaises(Exception, tokeniser.create_token)

from forest import Parser

class TestParser(unittest.TestCase):
    def test_something(self):
        tokens = {"ECHO": 1, "STRSTART" : 2, "STRING" : 3, "STRSTOP" : 4}
        parser = Parser(tokens)
        self.assertEqual(parser.run_parser(), True)
        
if __name__ == '__main__':
    unittest.main()
