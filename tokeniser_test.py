import unittest

class TestInterpreter(unittest.TestCase):

    def test_method_returns_echo_token_when_passed_e(self):
        from forest import Interpreter
        interpreter = Interpreter("e")
        self.assertEqual(interpreter.tokeniser(), ['ECHO', 'e'])


