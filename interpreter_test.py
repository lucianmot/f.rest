import unittest
from forest import Interpreter, Tokeniser, Parser, ASTString, ASTEcho, ASTEquals, ASTConditional, ASTModulus, ASTInteger

class TestFizzBuzzFeature(unittest.TestCase):
    def test_simple_fizzbuzz_feature(self):
       interpreter = Interpreter("WALK_PATH_IF_SEE^30^(*)>^15^OvO^0^echo^<<fizzbuzz>>")
       self.assertEqual(interpreter.response(), "Forest says: fizzbuzz")

    def test_simple_fizz_feature(self):
       interpreter = Interpreter("WALK_PATH_IF_SEE^6^(*)>^3^OvO^0^echo^<<fizz>>")
       self.assertEqual(interpreter.response(), "Forest says: fizz")

    def test_simple_buzz_feature(self):
       interpreter = Interpreter("WALK_PATH_IF_SEE^10^(*)>^5^OvO^0^echo^<<buzz>>")
       self.assertEqual(interpreter.response(), "Forest says: buzz")

class TestInterpreter(unittest.TestCase):
    def test_intepreter_should_be_initialized_with_text(self):
        interpreter = Interpreter("echo")
        self.assertEqual(interpreter.text, "echo")

    def test_interpreter_should_return_e_when_user_enters_e(self):
        interpreter = Interpreter("echo^<<e>>")
        self.assertEqual(interpreter.response(), "Forest says: e")

    def test_interpreter_should_return_A_when_user_enters_A(self):
        interpreter = Interpreter("echo^<<A>>")
        self.assertEqual(interpreter.response(), "Forest says: A")

    @unittest.skip("reason bug")
    def test_interpreter_should_return_integer_when_user_enters_4(self):
        interpreter = Interpreter("echo^<<4>>")
        self.assertEqual(interpreter.response(), "Forest says: 4")

    def test_interpreter_should_return_Hello_World(self):
        interpreter = Interpreter("echo^<<Hello World!>>")
        self.assertEqual(interpreter.response(), "Forest says: Hello World!")

    def test_interpreter_should_raise_exception_when_invalid_syntax(self):
        interpreter = Interpreter("Hello")
        self.assertRaises(Exception, interpreter.response)

    def test_interpreter_visit_tree_should_return_user_output(self):
        interpreter = Interpreter("")
        tokens = [{"ECHO": "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "Hello World!"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_1()
        self.assertEqual(interpreter.visit_tree(ast_output), "Forest says: Hello World!")

    def test_interpreter_visit_tree_should_return_more_user_output(self):
        interpreter = Interpreter("")
        tokens = [{"ECHO": "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "Hello Rangers!"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_1()
        self.assertEqual(interpreter.visit_tree(ast_output), "Forest says: Hello Rangers!")

class TestParser(unittest.TestCase):
    def test_valid_sequence_of_string_tokens_returns_true(self):
        tokens = [{"ECHO": "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "string"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        self.assertEqual(parser.match_grammar_rule(), "rule_1")

    def test_valid_sequence_of_string_tokens_with_comparison_returns_true(self):
        tokens = [{"STRSTART" : "<<"}, {"STRING_CONTENT" : "string"}, {"STRSTOP" : ">>"}, {"EQUALS": "OvO"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "string"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        self.assertEqual(parser.match_grammar_rule(), "rule_3")

    def test_invalid_sequence_of_string_tokens_returns_false(self):
        tokens = [{"ECHO": "echo"}, {"STRING_CONTENT" : "string"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        self.assertRaises(Exception, parser.match_grammar_rule)

    def test_valid_sequence_of_integer_tokens_returns_true(self):
        tokens = [{"ECHO": "echo"}, {"INTEGER": 8}]
        parser = Parser(tokens)
        self.assertEqual(parser.match_grammar_rule(), "rule_2")

    def test_invalid_sequence_of_integer_tokens_returns_false(self):
        tokens = [{"INTEGER": 8}, {"ECHO": "echo"}]
        parser = Parser(tokens)
        self.assertRaises(Exception, parser.match_grammar_rule)

    def test_create_ast_echo_for_grammar_rule_1(self):
        tokens = [{"ECHO": "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "mystring"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_1()
        self.assertIsInstance(ast_output, ASTEcho)

    def test_create_ast_echo_with_child_for_grammar_rule_1(self):
        tokens = [{"ECHO": "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "mystring"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_1()
        self.assertIsInstance(ast_output.expr, ASTString)

    def test_create_ast_echo_with_child_string_with_value_for_grammar_rule_1(self):
        tokens = [{"ECHO": "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "anotherstring"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_1()
        self.assertEqual(ast_output.expr.value, "anotherstring")

    def test_create_ast_equals_for_grammar_rule_3(self):
        tokens = [{"STRSTART" : "<<"}, {"STRING_CONTENT": "Hello Forest"}, {"STRSTOP" : ">>"}, {"EQUALS": "OvO"}, {"STRSTART" : "<<"}, {"STRING_CONTENT": "Hello Forest"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_3()
        self.assertIsInstance(ast_output, ASTEquals)

    def test_create_ast_equals_for_grammar_rule_3_string_value_operand_1(self):
        tokens = [{"STRSTART" : "<<"}, {"STRING_CONTENT": "Hello Forest"}, {"STRSTOP" : ">>"}, {"EQUALS": "OvO"}, {"STRSTART" : "<<"}, {"STRING_CONTENT": "Hello Forest again"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_3()
        self.assertEqual(ast_output.operand1.value, "Hello Forest")

    def test_create_ast_equals_for_grammar_rule_3_string_value_operand_3(self):
        tokens = [{"STRSTART" : "<<"}, {"STRING_CONTENT": "Hello Forest"}, {"STRSTOP" : ">>"}, {"EQUALS": "OvO"}, {"STRSTART" : "<<"}, {"STRING_CONTENT": "Hello Forest again"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        ast_output = parser.create_ast_for_rule_3()
        self.assertEqual(ast_output.operand2.value, "Hello Forest again")

    def test_valid_sequence_for_fizzbuzz_returns_grammar_rule4(self):
        tokens = [{"IF_START" : "WALK_PATH_IF_SEE"}, {"INTEGER" : "30"}, {"MODULUS" : "(*)>"}, {"INTEGER" : "15"}, {"EQUALS" : "OvO"}, {"INTEGER" : "0"}, {"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "fizzbuzz"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        self.assertEqual(parser.match_grammar_rule(), "rule_4")

class TestParserASTForGrammarRule4(unittest.TestCase):

    def setUp(self):
        tokens = [{"IF_START" : "WALK_PATH_IF_SEE"}, {"INTEGER" : 30}, {"MODULUS" : "(*)>"}, {"INTEGER" : 15}, {"EQUALS" : "OvO"}, {"INTEGER" : 0}, {"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "fizzbuzz"}, {"STRSTOP" : ">>"}]
        parser = Parser(tokens)
        self.ast_output = parser.create_ast_for_rule_4()

    def test_create_ast_equals_for_grammar_rule_4(self):
        self.assertIsInstance(self.ast_output, ASTConditional)

    def test_create_ast_equals_for_grammar_rule_4_then_branch(self):
        self.assertIsInstance(self.ast_output.then_branch, ASTEcho)

    def test_create_ast_equals_for_grammar_rule_4_then_branch_echos_is_a_string(self):
        self.assertIsInstance(self.ast_output.then_branch.expr, ASTString)

    def test_create_ast_equals_for_grammar_rule_4_then_branch_echos_is_a_string_with_value_fizzbuzz(self):
        self.assertEqual(self.ast_output.then_branch.expr.value, "fizzbuzz")

    def test_create_ast_equals_for_grammar_rule_4_ast_equal_on_expression_branch(self):
        self.assertIsInstance(self.ast_output.expr_branch, ASTEquals)

    def test_create_ast_equals_for_grammar_rule_4_ASTEqual_left_branch_has_modulus(self):
        self.assertIsInstance(self.ast_output.expr_branch.operand1, ASTModulus)

    def test_create_ast_equals_for_grammar_rule_4_Modulus_int_left_branch(self):
        self.assertIsInstance(self.ast_output.expr_branch.operand1.operand1, ASTInteger)

    def test_create_ast_euals_for_grammar_rule_4_Modulus_int_left_branch_value_30(self):
        self.assertEqual(self.ast_output.expr_branch.operand1.operand1.value, 30)

    def test_create_ast_equals_for_grammar_rule_4_Modulus_int_right_branch(self):
        self.assertIsInstance(self.ast_output.expr_branch.operand1.operand2, ASTInteger)

    def test_create_ast_euals_for_grammar_rule_4_Modulus_int_right_branch_value_15(self):
        self.assertEqual(self.ast_output.expr_branch.operand1.operand2.value, 15)

    def test_create_ast_equals_for_grammar_rule_4_equal_right_branch(self):
        self.assertIsInstance(self.ast_output.expr_branch.operand2, ASTInteger)

    def test_create_ast_euals_for_grammar_rule_4_equal_right_branch_value_0(self):
        self.assertEqual(self.ast_output.expr_branch.operand2.value, 0)

class TestInterpreterForGrammarRule4(unittest.TestCase):

    def test_visit_modulus_returns_0(self):
        interpreter = Interpreter("")
        ast_mod = ASTModulus(ASTInteger(15), ASTInteger(5))
        self.assertEqual(interpreter.visit_ast_modulus(ast_mod), 0)

    def test_visit_modulus_returns_1(self):
        interpreter = Interpreter("")
        ast_mod = ASTModulus(ASTInteger(16), ASTInteger(5))
        self.assertEqual(interpreter.visit_ast_modulus(ast_mod), 1)

    def test_visit_equal_returns_true(self):
        interpreter = Interpreter("")
        ast_mod = ASTModulus(ASTInteger(16), ASTInteger(5))
        ast_equal = ASTEquals(ast_mod, ASTInteger(1))
        self.assertEqual(interpreter.visit_ast_equals(ast_equal), True)

    def test_visit_equal_returns_false(self):
        interpreter = Interpreter("")
        ast_mod = ASTModulus(ASTInteger(16), ASTInteger(5))
        ast_equal = ASTEquals(ast_mod, ASTInteger(2))
        self.assertEqual(interpreter.visit_ast_equals(ast_equal), False)

    def test_visit_conditional_returns_FizzBuzz(self):
        interpreter = Interpreter("")
        ast_mod = ASTModulus(ASTInteger(30), ASTInteger(15))
        ast_equal = ASTEquals(ast_mod, ASTInteger(0))
        ast_echo = ASTEcho(ASTString("FizzBuzz"))
        ast_conditional = ASTConditional(ast_equal, ast_echo, "else...")
        self.assertEqual(interpreter.visit_ast_conditional(ast_conditional), "Forest says: FizzBuzz")

class TestInterpreterForGrammarRule3(unittest.TestCase):

    def test_visit_equal_two_same_strings_returns_true(self):
        interpreter = Interpreter("")
        ast_equal = ASTEquals(ASTString("hello"), ASTString("hello"))
        self.assertEqual(interpreter.visit_ast_equals(ast_equal), True)

    def test_visit_equal_two_different_strings_returns_false(self):
        interpreter = Interpreter("")
        ast_equal = ASTEquals(ASTString("hello"), ASTString("not hello"))
        self.assertEqual(interpreter.visit_ast_equals(ast_equal), False)

class TestAST(unittest.TestCase):
    def test_AST_String_node_is_created_with_the_string_value(self):
        string_ast_node = ASTString("Hello World")
        self.assertEqual(string_ast_node.value, "Hello World")

    def test_AST_Echo_node_is_created_with_the_child_string_node_attached(self):
        string_ast_node = ASTString("Hello World")
        echo_ast_node = ASTEcho(string_ast_node)
        self.assertEqual(echo_ast_node.expr.value, "Hello World")

class TestTokeniser(unittest.TestCase):

    def test_method_returns_string_token_when_passed_e(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo^<<e>>")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "e"}, {"STRSTOP" : ">>"}])

    def test_method_returns_string_token_when_passed_caps_z(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo^<<Z>>")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "Z"}, {"STRSTOP" : ">>"}])

    def test_tokeniser_recognises_all_tokens_in_text(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("echo^<<Hello Test!>>")
        self.assertEqual(tokeniser.create_tokens(), [{"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "Hello Test!"}, {"STRSTOP" : ">>"}])

    def test_tokeniser_recognises_that_true_is_true(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("true")
        self.assertEqual(tokeniser.create_tokens(), [{"BOOLEAN" : "true"}])

    def test_tokeniser_recognises_that_false_is_false(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("false")
        self.assertEqual(tokeniser.create_tokens(), [{"BOOLEAN" : "false"}])

    def test_method_returns_integer_item_when_passed_number(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("9")
        self.assertEqual(tokeniser.create_tokens(), [{"INTEGER" : '9'}])

    def test_method_returns_string_token_when_passed_a_string(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("<<a>>")
        self.assertEqual(tokeniser.create_tokens(), [{"STRSTART" : "<<"}, {"STRING_CONTENT" : "a"}, {"STRSTOP" : ">>"}])

    def test_method_returns_array_split_by_delimiter(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("true^4")
        self.assertEqual(tokeniser.split_input(), ["true", "4"])

    def test_method_returns_string_token_when_passed_a_longer_string(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("<<a lot of text>>")
        self.assertEqual(tokeniser.create_tokens(), [{"STRSTART" : "<<"}, {"STRING_CONTENT" : "a lot of text"}, {"STRSTOP" : ">>"}])

    def test_method_returns_comparison_token_for_owl_operator(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("OvO")
        self.assertEqual(tokeniser.create_tokens(), [{"EQUALS" : "OvO"}])

    def test_method_returns_comparison_token_and_bool_for_owl_operator_with_bools(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("true^OvO^false")
        self.assertEqual(tokeniser.create_tokens(), [{"BOOLEAN" : "true"}, {"EQUALS" : "OvO"}, {"BOOLEAN" : "false"}])

    def test_method_returns_tokens_for_String_comparison(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("<<this>>^OvO^<<that>>")
        self.assertEqual(tokeniser.create_tokens(), [{"STRSTART" : "<<"}, {"STRING_CONTENT" : "this"}, {"STRSTOP" : ">>"}, {"EQUALS" : "OvO"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "that"}, {"STRSTOP" : ">>"}])

    def test_method_returns_dead_owl_when_passed_in_with_integers(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("7^XvX^8")
        self.assertEqual(tokeniser.create_tokens(), [{"INTEGER" : "7"}, {"NOT_EQUAL" : "XvX"}, {"INTEGER" : "8"}])

    def test_method_returns_dead_owl_when_passed_in_with_bools(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("true^XvX^false")
        self.assertEqual(tokeniser.create_tokens(), [{"BOOLEAN" : "true"}, {"NOT_EQUAL" : "XvX"}, {"BOOLEAN" : "false"}])

    def test_method_returns_dead_owl_tokens_when_passed_with_strings(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("<<Superman>>^XvX^<<Batman>>")
        self.assertEqual(tokeniser.create_tokens(), [{"STRSTART" : "<<"}, {"STRING_CONTENT" : "Superman"}, {"STRSTOP" : ">>"}, {"NOT_EQUAL" : "XvX"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "Batman"}, {"STRSTOP" : ">>"}])

    def test_method_returns_crow_operator_when_passed_in(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("(*)>")
        self.assertEqual(tokeniser.create_tokens(), [{"MODULUS" : "(*)>"}])

    def test_method_returns_crow_operator_when_passed_in_with_integers(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("5^(*)>^2")
        self.assertEqual(tokeniser.create_tokens(), [{"INTEGER" : "5"}, {"MODULUS" : "(*)>"}, {"INTEGER" : "2"}])

    def test_tokeniser_recognises_beginning_of_if_statement(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("WALK_PATH_IF_SEE")
        self.assertEqual(tokeniser.create_tokens(), [{"IF_START" : "WALK_PATH_IF_SEE"}])

    def test_tokeniser_recognises_beginning_of_if_statement_with_argument(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("WALK_PATH_IF_SEE^6")
        self.assertEqual(tokeniser.create_tokens(), [{"IF_START" : "WALK_PATH_IF_SEE"}, {"INTEGER" : "6"}])

    def test_tokeniser_recognises_beginning_of_if_statement_with_boolean(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("WALK_PATH_IF_SEE^true")
        self.assertEqual(tokeniser.create_tokens(), [{"IF_START" : "WALK_PATH_IF_SEE"}, {"BOOLEAN" : "true"}])

    def test_tokeniser_recognises_end_of_expression(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("CAMP")
        self.assertEqual(tokeniser.create_tokens(), [{"END" : "CAMP"}])

    def test_tokeniser_tokenises_if_end_statement(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("WALK_PATH_IF_SEE^CAMP")
        self.assertEqual(tokeniser.create_tokens(), [{"IF_START" : "WALK_PATH_IF_SEE"}, {"END" : "CAMP"}])

    def test_tokeniser_tokenises_fizzbuzz_statement(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("WALK_PATH_IF_SEE^30^(*)>^15^OvO^0^echo^<<fizzbuzz>>")
        self.assertEqual(tokeniser.create_tokens(), [{"IF_START" : "WALK_PATH_IF_SEE"}, {"INTEGER" : "30"}, {"MODULUS" : "(*)>"}, {"INTEGER" : "15"}, {"EQUALS" : "OvO"}, {"INTEGER" : "0"}, {"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "fizzbuzz"}, {"STRSTOP" : ">>"}])

    def test_tokeniser_tokenises_fizzbuzz_statement_with_end(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("WALK_PATH_IF_SEE^30^(*)>^15^OvO^0^echo^<<fizzbuzz>>^CAMP")
        self.assertEqual(tokeniser.create_tokens(), [{"IF_START" : "WALK_PATH_IF_SEE"}, {"INTEGER" : "30"}, {"MODULUS" : "(*)>"}, {"INTEGER" : "15"}, {"EQUALS" : "OvO"}, {"INTEGER" : "0"}, {"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRING_CONTENT" : "fizzbuzz"}, {"STRSTOP" : ">>"}, {"END" : "CAMP"}])

    def test_tokenise_variable_assigment(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("BACKPACK")
        self.assertEqual(tokeniser.create_tokens(), [{"VARIABLE" : "BACKPACK"}])

    def test_tokenise_variable_assigment_assigner(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("PACK_WITH")
        self.assertEqual(tokeniser.create_tokens(), [{"ASSIGNMENT" : "PACK_WITH"}])

    def test_tokenise_variable_assignment_with_a_string(self):
        from forest import Tokeniser
        tokeniser = Tokeniser("BACKPACK:arnold^PACK_WITH^<<pikachu>>")
        self.assertEqual(tokeniser.create_tokens(), [{"VARIABLE" : "BACKPACK"}, {"VARIABLE_NAME" : "arnold"}, {"ASSIGNMENT" : "PACK_WITH"},
        {"STRSTART" : "<<"}, {"STRING_CONTENT" : "pikachu"}, {"STRSTOP" : ">>"}])
    

if __name__ == '__main__':
    unittest.main()
