import unittest

class TestTokeniser(unittest.TestCase):

    def test_method_returns_string_token_when_passed_e(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo<<e>>")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRSTOP" : ">>"}, {"STRING_CONTENT" : "e"}])

    def test_method_returns_string_token_when_passed_a(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo<<a>>")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRSTOP" : ">>"},  {"STRING_CONTENT" : "a"}])

    def test_method_returns_string_token_when_passed_caps_z(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo<<Z>>")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRSTOP" : ">>"}, {"STRING_CONTENT" : "Z"}])

    def test_tokeniser_recognises_all_tokens_in_text(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo<<Hello Test!>>true5 ")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"BOOLEAN" : "true"}, {"INTEGER" : "5"}, {"WHITESPACE" : " "}, {"STRSTART" : "<<"}, {"STRSTOP" : ">>"}, {"STRING_CONTENT" : "Hello Test!"}])
    
    def test_tokeniser_recognises_that_true_is_true(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("true")
        self.assertEqual(tokeniser.create_tokens(), [{"BOOLEAN" : "true"}])
        
    def test_tokeniser_recognises_that_false_is_false(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("false")
        self.assertEqual(tokeniser.create_tokens(), [{"BOOLEAN" : "false"}])

    def test_method_returns_integer_item_when_passed_number(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("9")
        self.assertEqual(tokeniser.create_tokens(), [{"INTEGER" : '9'}])