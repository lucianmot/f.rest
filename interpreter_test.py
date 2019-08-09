import unittest
from forest import Interpreter, Tokeniser, Parser

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

    def test_method_raises_exception_when_strstart_is_not_present(self):
        tokeniser = Tokeniser("echohello>>")
        self.assertRaises(Exception, tokeniser.create_token)

    def test_method_raises_exception_when_strstop_is_not_present(self):
        tokeniser = Tokeniser("echo<<hello")
        self.assertRaises(Exception, tokeniser.create_token)

class TestParser(unittest.TestCase):
    def test_valid_sequence_of_string_tokens_returns_true(self):
        tokens = {"ECHO": "echo", "STRSTART" : "<<", "STRING" : "string", "STRSTOP" : ">>"}
        parser = Parser(tokens)
        self.assertEqual(parser.match_grammar_rule(), "grammar_rule_1")

    def test_invalid_sequence_of_string_tokens_returns_false(self):
        tokens = {"ECHO": "echo", "STRING" : "string", "STRSTOP" : ">>"}
        parser = Parser(tokens)
        self.assertRaises(Exception, parser.match_grammar_rule)

    def test_valid_sequence_of_integer_tokens_returns_true(self):
        tokens = {"ECHO": "echo", "INTEGER": 8}
        parser = Parser(tokens)
        self.assertEqual(parser.match_grammar_rule(), "grammar_rule_2")

    def test_invalid_sequence_of_integer_tokens_returns_false(self):
        tokens = {"INTEGER": 8, "ECHO": "echo"}
        parser = Parser(tokens)
        self.assertRaises(Exception, parser.match_grammar_rule)


if __name__ == '__main__':
    unittest.main()
