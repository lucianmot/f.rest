import unittest

class TestInterpreter(unittest.TestCase):

    def test_method_returns_string_token_when_passed_e(self):
        from forest import Interpreter
        interpreter = Interpreter("echo e")
        self.assertEqual(interpreter.tokeniser(), [{"ECHO" : "echo"}, {"STRING" : "e"}])

    def test_method_returns_string_token_when_passed_a(self):
        from forest import Interpreter
        interpreter = Interpreter("echo a")
        self.assertEqual(interpreter.tokeniser(), [{"ECHO" : "echo"}, {"STRING" : "a"}])

    def test_method_returns_string_token_when_passed_caps_z(self):
        from forest import Interpreter
        interpreter = Interpreter("echo Z")
        self.assertEqual(interpreter.tokeniser(), [{"ECHO" : "echo"}, {"STRING" : "Z"}])

    def test_method_returns_exception_when_passed_number(self):
        from forest import Interpreter
        interpreter = Interpreter("9")
        self.assertRaises(Exception, interpreter.tokeniser)

    
