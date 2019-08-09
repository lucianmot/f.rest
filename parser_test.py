import unittest

class TestParser(unittest.TestCase):
    def test_something(self):
        from forest import Parser
        tokens = {"ECHO": 1, "STRSTART" : 2, "STRING" : 3, "STRSTOP" : 4}
        parser = Parser(tokens)
        self.assertEqual(parser.run_parser(), True)
        