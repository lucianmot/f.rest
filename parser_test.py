import unittest
from forest import Parser

class TestParser(unittest.TestCase):
    def test_valid_sequence_of_tokens_returns_true(self):
        tokens = {"ECHO": 1, "STRSTART" : 2, "STRING" : 3, "STRSTOP" : 4}
        parser = Parser(tokens)
        self.assertEqual(parser.run_parser(), True)
        