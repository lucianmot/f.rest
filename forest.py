import re

TOKENS =   [re.compile(r'(?P<VARIABLE>BACKPACK)'), re.compile(r'(?P<IF_START>WALK_PATH_IF_SEE)'),
            re.compile(r'(?P<ECHO>echo)'), re.compile(r'(?P<BOOLEAN>true|false)'), re.compile(r'(?P<MODULUS>\(\*\)\>)'), 
            re.compile(r'(?P<EQUALS>OvO)'), re.compile(r'(?P<NOT_EQUAL>XvX)'), 
            re.compile(r'(?P<INTEGER>[\d]+)'), re.compile(r'(?P<STRSTART><<)'), 
            re.compile(r'(?:<<)(?P<STRING_CONTENT>.+)(?:>>)'), re.compile(r'(?P<STRSTOP>>>)'), 
            re.compile(r'(?P<END>CAMP)')]

class Interpreter(object):
    def __init__(self, text):
        self.text = text

    def response(self):
        tokeniser = Tokeniser(self.text)
        token = tokeniser.create_tokens()
        parser = Parser(token)
        parser.match_grammar_rule()
        ast_output = parser.create_ast_for_rule_1()
        return self.visit_tree(ast_output)

    def visit_tree(self, ast_output):
        return self.visit_ast_echo(ast_output)

    def visit_ast_echo(self, ast_echo_node):
        return "Forest says: " + ast_echo_node.expr.value

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
        self.grammar_rule_1 = GrammarRule("grammar_rule_1",["ECHO", "STRSTART", "STRING_CONTENT", "STRSTOP"])
        self.grammar_rule_2 = GrammarRule("grammar_rule_2",["ECHO", "INTEGER"])
        self.grammar_rule_3 = GrammarRule("grammar_rule_3",["STRING_CONTENT", "EQUALS", "STRING_CONTENT"])
        self.rules = [self.grammar_rule_1, self.grammar_rule_2, self.grammar_rule_3]

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
        test = self.get_token_by_key()
        return ASTEcho(ASTString(test))

    def create_ast_for_rule_3(self):
        str_token1 = self.tokens[0]
        str_token3 = self.tokens[2]
        return ASTEquals(ASTString(str_token1["STRING_CONTENT"]), ASTString(str_token3["STRING_CONTENT"]))

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
