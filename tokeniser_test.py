import unittest

class TestTokeniser(unittest.TestCase):

    def test_method_returns_string_token_when_passed_e(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo<<e nobody can stop me>>")
        self.assertEqual(tokeniser.create_token(), {"ECHO" : "echo", "STRSTART" : "<<", "STRING" : "e", "STRSTOP" : ">>"})

    def test_method_returns_string_token_when_passed_a(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo<<akill everything>>")
        self.assertEqual(tokeniser.create_token(), {"ECHO" : "echo", "STRSTART" : "<<", "STRING" : "a", "STRSTOP" : ">>"})

    def test_method_returns_string_token_when_passed_caps_z(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo<<Zsomseothsosgidsfgmsodfgjdsfiojdsfiogj>>")
        self.assertEqual(tokeniser.create_token(), {"ECHO" : "echo", "STRSTART" : "<<", "STRING" : "Z", "STRSTOP" : ">>"})

    def test_method_returns_exception_when_passed_number(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("9something eslsesgojdfgjsdofigjdfgpoop")
        self.assertRaises(Exception, tokeniser.create_token)
