import unittest
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
