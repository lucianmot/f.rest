import unittest
from forest import Interpreter, Tokeniser, Parser, ASTString, ASTEcho

class TestInterpreter(unittest.TestCase):
    def test_intepreter_should_be_initialized_with_text(self):
        interpreter = Interpreter("echo")
        self.assertEqual(interpreter.text, "echo")

    def test_interpreter_should_return_e_when_user_enters_e(self):
        interpreter = Interpreter("echo<<e>>")
        self.assertEqual(interpreter.response(), "Forest says: e")

    def test_interpreter_should_return_A_when_user_enters_A(self):
        interpreter = Interpreter("echo<<A>>")
        self.assertEqual(interpreter.response(), "Forest says: A")

    def test_interpreter_should_return_integer_when_user_enters_4(self):
        interpreter = Interpreter("echo<<4>>")
        self.assertEqual(interpreter.response(), "Forest says: 4")

    def test_interpreter_should_return_Hello_World(self):
        interpreter = Interpreter("echo<<Hello World!>>")
        self.assertEqual(interpreter.response(), "Forest says: Hello World!")

    def test_interpreter_should_raise_exception_when_invalid_syntax(self):
        interpreter = Interpreter("Hello")
        self.assertRaises(Exception, interpreter.response)

    def test_interpreter_visit_tree_should_return_user_output(self):
        interpreter = Interpreter("")
        tokens = {"ECHO": "echo", "STRSTART" : "<<", "STRING" : "Hello World!", "STRSTOP" : ">>"}
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_1()
        self.assertEqual(interpreter.visit_tree(ast_output), "Forest says: Hello World!")

    def test_interpreter_visit_tree_should_return_more_user_output(self):
        interpreter = Interpreter("")
        tokens = {"ECHO": "echo", "STRSTART" : "<<", "STRING" : "Hello Rangers!", "STRSTOP" : ">>"}
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_1()
        self.assertEqual(interpreter.visit_tree(ast_output), "Forest says: Hello Rangers!")

class TestTokeniser(unittest.TestCase):

    def test_method_returns_string_token_when_passed_e(self):
        tokeniser = Tokeniser("echo<<e>>")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRSTOP" : ">>"}, {"STRING_CONTENT" : "e"}])

    def test_method_returns_string_token_when_passed_a(self):
        tokeniser = Tokeniser("echo<<a>>")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRSTOP" : ">>"}, {"STRING_CONTENT" : "a"}])

    def test_method_returns_string_token_when_passed_caps_z(self):
        tokeniser = Tokeniser("echo<<Z>>")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRSTOP" : ">>"}, {"STRING_CONTENT" : "Z"}])

    def test_method_returns_integer_item_when_passed_number(self):
        tokeniser = Tokeniser("9")
        self.assertEqual(tokeniser.create_tokens(), [{"INTEGER" : '9'}])

    # THOSE EXCEPTIONS SHOULD LIVE IN THE INTERPRETER
    #def test_method_raises_exception_when_strstart_is_not_present(self):
    #    tokeniser = Tokeniser("echohello>>")
    #    self.assertRaises(Exception, tokeniser.create_token)

    #def test_method_raises_exception_when_strstop_is_not_present(self):
    #    tokeniser = Tokeniser("echo<<hello")
    #    self.assertRaises(Exception, tokeniser.create_token)
    
    def test_tokeniser_recognises_that_true_is_true(self):
        tokeniser = Tokeniser("true")
        self.assertEqual(tokeniser.create_tokens(), [{"BOOLEAN" : "true"}])
    
    def test_tokeniser_recognises_that_false_is_false(self):
        tokeniser = Tokeniser("false")
        self.assertEqual(tokeniser.create_tokens(), [{"BOOLEAN" : "false"}])

    def test_tokeniser_recognises_all_tokens_in_text(self):
        tokeniser = Tokeniser("echo<<Hello Test!>>true5 ")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"BOOLEAN" : "true"}, {"INTEGER" : "5"}, {"WHITESPACE" : " "}, {"STRSTART" : "<<"}, {"STRSTOP" : ">>"}, {"STRING_CONTENT" : "Hello Test!"}])

class TestParser(unittest.TestCase):
    def test_valid_sequence_of_string_tokens_returns_true(self):
        tokens = {"ECHO": "echo", "STRSTART" : "<<", "STRING" : "string", "STRSTOP" : ">>"}
        parser = Parser(tokens)
        self.assertEqual(parser.match_grammar_rule(), "grammar_rule_1")

    def test_invalid_sequence_of_string_tokens_returns_false(self):
        tokens = {"ECHO": "echo", "STRING" : "string", "STRSTOP" : ">>"}
        parser = Parser(tokens)
        self.assertRaises(Exception, parser.match_grammar_rule)

    def test_valid_sequence_of_integer_tokens_returns_true(self):
        tokens = {"ECHO": "echo", "INTEGER": 8}
        parser = Parser(tokens)
        self.assertEqual(parser.match_grammar_rule(), "grammar_rule_2")

    def test_invalid_sequence_of_integer_tokens_returns_false(self):
        tokens = {"INTEGER": 8, "ECHO": "echo"}
        parser = Parser(tokens)
        self.assertRaises(Exception, parser.match_grammar_rule)

    def test_create_ast_echo_for_grammar_rule_1(self):
        tokens = {"ECHO": "echo", "STRSTART" : "<<", "STRING" : "mystring", "STRSTOP" : ">>"}
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_1()
        self.assertIsInstance(ast_output, ASTEcho)

    def test_create_ast_echo_with_child_for_grammar_rule_1(self):
        tokens = {"ECHO": "echo", "STRSTART" : "<<", "STRING" : "mystring", "STRSTOP" : ">>"}
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_1()
        self.assertIsInstance(ast_output.expr, ASTString)

    def test_create_ast_echo_with_child_string_with_value_for_grammar_rule_1(self):
        tokens = {"ECHO": "echo", "STRSTART" : "<<", "STRING" : "anotherstring", "STRSTOP" : ">>"}
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_1()
        self.assertEqual(ast_output.expr.value, "anotherstring")

class TestAST(unittest.TestCase):
    def test_AST_String_node_is_created_with_the_string_value(self):
        string_ast_node = ASTString("Hello World")
        self.assertEqual(string_ast_node.value, "Hello World")

    def test_AST_Echo_node_is_created_with_the_child_string_node_attached(self):
        string_ast_node = ASTString("Hello World")
        echo_ast_node = ASTEcho(string_ast_node)
        self.assertEqual(echo_ast_node.expr.value, "Hello World")

if __name__ == '__main__':
    unittest.main()
