import unittest

class TestInterpreter(unittest.TestCase):

    def test_interpreter_should_return_nothing_when_echo_with_empty_string(self):
        from forest import Interpreter
        interpreter = Interpreter("echo <<>>")
        self.assertEqual(interpreter.response(), "")
        