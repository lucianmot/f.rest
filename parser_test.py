import unittest
from forest import Parser

class TestParser(unittest.TestCase):
    def test_something(self):
        tokens = {"ECHO": 1, "STRSTART" : 2, "STRING" : 3, "STRSTOP" : 4}
        parser = Parser(tokens)
        self.assertEqual(parser.run_parser(), True)
        