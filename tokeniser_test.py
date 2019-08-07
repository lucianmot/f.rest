import unittest

class TestInterpreter(unittest.TestCase):

    def test_method_returns_string_token_when_passed_e(self):
        from forest import Interpreter
        interpreter = Interpreter("e")
        self.assertEqual(interpreter.tokeniser(), [{"STRING" : "e"}])

    def test_method_returns_string_token_when_passed_a(self):
        from forest import Interpreter
        interpreter = Interpreter("a")
        self.assertEqual(interpreter.tokeniser(), [{"STRING" : "a"}])

    def test_method_returns_string_token_when_passed_caps_z(self):
        from forest import Interpreter
        interpreter = Interpreter("Z")
        self.assertEqual(interpreter.tokeniser(), [{"STRING" : "Z"}])

    def test_method_returns_oops_when_passed_number(self):
        from forest import Interpreter
        interpreter = Interpreter("9")
        self.assertEqual(interpreter.tokeniser(), "oops")
