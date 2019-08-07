import unittest

class TestInterpreter(unittest.TestCase):

    def test_method_returns_string_token_when_passed_e(self):
        from forest import Interpreter
        interpreter = Interpreter("e")
        self.assertEqual(interpreter.tokeniser(), [{'STRING' : 'e'}])

    def test_method_returns_string_token_when_passed_a(self):
        from forest import Interpreter
        interpreter = Interpreter("a")
        self.assertEqual(interpreter.tokeniser(), [{'STRING' : 'a'}])
