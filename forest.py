import re

TOKENS =   [re.compile(r'(?P<IF_START>WALK_PATH_IF_SEE)'), re.compile(r'(?P<ECHO>echo)'),
            re.compile(r'(?P<BOOLEAN>true|false)'), re.compile(r'(?P<MODULUS>\(\*\)\>)'),
            re.compile(r'(?P<EQUALS>OvO)'), re.compile(r'(?P<NOT_EQUAL>XvX)'),
            re.compile(r'(?P<INTEGER>[\d]+)'), re.compile(r'(?P<STRSTART><<)'),
            re.compile(r'(?:<<)(?P<STRING_CONTENT>.+)(?:>>)'), re.compile(r'(?P<STRSTOP>>>)'),
            re.compile(r'(?P<END>CAMP)')]

class Interpreter(object):
    def __init__(self, text):
        self.text = text

    def response(self):
        tokeniser = Tokeniser(self.text)
        parser = Parser(tokeniser.create_tokens())
        return self.visit_tree(self._get_ast_method(parser))

    def visit_tree(self, ast_output):
        return self.visit_ast_echo(ast_output)

    def visit_ast_echo(self, ast_echo_node):
        return "Forest says: " + ast_echo_node.expr.value

    def _get_ast_method(self, parser):
        method_name = 'create_ast_for_' + parser.match_grammar_rule()
        ast_method = getattr(parser, method_name)
        return ast_method()


class Tokeniser(object):
    def __init__(self, text):
        self.text = text

    def create_tokens(self):
        input_array = self.split_input()
        results = []
        for item in input_array:
            for token in TOKENS:
                match_attempt = token.search(item)
                if match_attempt == None:
                    continue
                results.append(match_attempt.groupdict())

        return results

    def split_input(self):
        return self.text.split('^')

class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.grammar_rule_1 = GrammarRule("rule_1",["ECHO", "STRSTART", "STRING_CONTENT", "STRSTOP"])
        self.grammar_rule_2 = GrammarRule("rule_2",["ECHO", "INTEGER"])
        self.grammar_rule_3 = GrammarRule("rule_3",["STRING_CONTENT", "EQUALS", "STRING_CONTENT"])
        self.grammar_rule_4 = GrammarRule("rule_4",["IF_START", "INTEGER", "MODULUS", "INTEGER", "EQUALS", "INTEGER", "ECHO", "STRSTART", "STRING_CONTENT", "STRSTOP", "END"] )
        self.rules = [self.grammar_rule_1, self.grammar_rule_2, self.grammar_rule_3, self.grammar_rule_4]

    def user_input_tokens(self):
        parse_keys = []
        for item in self.tokens:
            for key in item.keys():
                parse_keys.append(key)

        return parse_keys

    def match_grammar_rule(self):
        for rule in self.rules:
            if rule.rule == self.user_input_tokens():
                return rule.rule_name
        raise Exception("Syntax Error")

    def create_ast_for_rule_1(self):
        user_input_string = self.get_token_by_key()
        return ASTEcho(ASTString(user_input_string))

    def create_ast_for_rule_3(self):
        str_token1 = self.tokens[0]
        str_token3 = self.tokens[2]
        return ASTEquals(ASTString(str_token1["STRING_CONTENT"]), ASTString(str_token3["STRING_CONTENT"]))

    def create_ast_for_rule_4(self):
        int_token1 = self.tokens[1]
        integer_operand1 = ASTInteger(int_token1["INTEGER"])
        modulus_operator = ASTModulus(integer_operand1, "Academy")
        expr_branch = ASTEquals(modulus_operator, "world")
        return ASTConditional(expr_branch, "Jo", "Aleks")

    def get_token_by_key(self):
        for item in self.tokens:
            if "STRING_CONTENT" in item:
                return item["STRING_CONTENT"]

class GrammarRule(object):
    def __init__(self, rule_name, rule):
        self.rule_name = rule_name
        self.rule = rule

class ASTString(object):
    def __init__(self, string):
        self.value = string

class ASTEcho(object):
    def __init__(self, expr):
        self.expr = expr

class ASTEquals(object):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

class ASTConditional(object):
    def __init__(self, expr_branch, then_branch, else_branch):
        self.expr_branch = expr_branch
        self.then_branch = then_branch
        self.else_branch = else_branch

class ASTModulus(object):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

class ASTInteger(object):
    def __init__(self, value):
        self.value = value
