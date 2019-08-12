import unittest

class TestTokeniser(unittest.TestCase):

    def test_method_returns_string_token_when_passed_e(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo<<e>>")
        self.assertEqual(tokeniser.create_tokens(), {"ECHO" : "echo", "STRSTART" : "<<", "STRING" : "e", "STRSTOP" : ">>"})

    def test_method_returns_string_token_when_passed_a(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo<<a>>")
        self.assertEqual(tokeniser.create_tokens(), {"ECHO" : "echo", "STRSTART" : "<<", "STRING" : "a", "STRSTOP" : ">>"})

    def test_method_returns_string_token_when_passed_caps_z(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo<<Z>>")
        self.assertEqual(tokeniser.create_tokens(), {"ECHO" : "echo", "STRSTART" : "<<", "STRING" : "Z", "STRSTOP" : ">>"})


