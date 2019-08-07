import unittest

class TestInterpreter(unittest.TestCase):

    def test_interpreter_should_return_e_when_user_enters_e(self):
        from forest import Interpreter
        interpreter = Interpreter("e")
        self.assertEqual(interpreter.response(), "e")

    def test_interpreter_should_return_A_when_user_enters_A(self):
        from forest import Interpreter
        interpreter = Interpreter("A")
        self.assertEqual(interpreter.response(), "A")

    def test_interpreter_should_return_Exception_when_user_enters_4(self):
        from forest import Interpreter
        interpreter = Interpreter("4")
        self.assertRaises(Exception, interpreter.response)

    # def test_interpreter_should_return_nothing_when_echo_with_empty_string(self):
    #     from forest import Interpreter
    #     interpreter = Interpreter("echo <<>>")
    #     self.assertEqual(interpreter.response(), "")

    # def test_interpreter_should_return_a_when_echo_with_a(self):
    #     from forest import Interpreter
    #     interpreter = Interpreter("echo <<a>>")
    #     self.assertEqual(interpreter.response(), "a")

    # def test_interpreter_should_return_hello_when_echo_with_hello(self):
    #     from forest import Interpreter
    #     interpreter = Interpreter("echo <<hello>>")
    #     self.assertEqual(interpreter.response(), "hello")

    # def test_interpreter_should_return_hello_world_when_echo_with_hello_world(self):
    #     from forest import Interpreter
    #     interpreter = Interpreter("echo <<Hello, world!>>")
    #     self.assertEqual(interpreter.response(), "Hello, world!")
