import unittest

class TestInterpreter(unittest.TestCase):

    def test_interpreter_should_return_e_when_user_enters_e(self):
        from forest import Interpreter
        interpreter = Interpreter("echo<<e>>")
        self.assertEqual(interpreter.response(), "e")

    def test_interpreter_should_return_A_when_user_enters_A(self):
        from forest import Interpreter
        interpreter = Interpreter("echo<<A>>")
        self.assertEqual(interpreter.response(), "A")

    def test_interpreter_should_return_Exception_when_user_enters_4(self):
        from forest import Interpreter
        interpreter = Interpreter("echo<<4>>")
        self.assertEqual(interpreter.response(), "4")

    def test_interpreter_should_return_Hello_World(self):
        from forest import Interpreter
        interpreter = Interpreter("echo<<Hello World!>>")
        self.assertEqual(interpreter.response(), "Hello World!")
