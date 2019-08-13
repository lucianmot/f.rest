import unittest

class TestTokeniser(unittest.TestCase):

    def test_method_returns_string_token_when_passed_e(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo^<<e>>")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "e"}, {"STRSTOP" : ">>"}])

    def test_method_returns_string_token_when_passed_caps_z(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo^<<Z>>")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "Z"}, {"STRSTOP" : ">>"}])

    def test_tokeniser_recognises_all_tokens_in_text(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo^<<Hello Test!>>")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "Hello Test!"}, {"STRSTOP" : ">>"}])
    
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

    def test_method_returns_string_token_when_passed_a_string(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("<<a>>")
        self.assertEqual(tokeniser.create_tokens(), [{"STRSTART" : "<<"}, {"STRING_CONTENT" : "a"}, {"STRSTOP" : ">>"}])

    def test_method_returns_array_split_by_delimiter(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("true^4")
        self.assertEqual(tokeniser.split_input(), ["true", "4"])
    
    def test_method_returns_string_token_when_passed_a_longer_string(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("<<a lot of text>>")
        self.assertEqual(tokeniser.create_tokens(), [{"STRSTART" : "<<"}, {"STRING_CONTENT" : "a lot of text"}, {"STRSTOP" : ">>"}])