import re

TOKENS =    [re.compile(r'(?P<ECHO>echo)'), re.compile(r'(?P<BOOLEAN>true|false)'), re.compile(r'(?P<INTEGER>\d)'),
            re.compile(r'(?P<WHITESPACE>\s)'), re.compile(r'(?P<STRSTART><<)'), re.compile(r'(?P<STRSTOP>>>)'),
            re.compile(r'(?:<<)(?P<STRING_CONTENT>.+)(?:>>)')]

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

# checks if input starts with echo - delete if not used
    def isecho(self):
        if bool(re.match("echo", self.text)) == True:
            return True
        else:
            return False

    def create_tokens(self):
        results = []
        for token in TOKENS:
            match_attempt = token.search(self.text)
            if match_attempt == None:
                continue
            results.append(match_attempt.groupdict())

        return results 

class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.grammar_rule_1 = GrammarRule("grammar_rule_1",["ECHO", "STRSTART", "STRING", "STRSTOP"])
        self.grammar_rule_2 = GrammarRule("grammar_rule_2",["ECHO", "INTEGER"])
        self.rules = [self.grammar_rule_1, self.grammar_rule_2]

    def user_input_tokens(self):
        parse_keys = []
        for key in self.tokens:
            parse_keys.append(key)
        return parse_keys

    def match_grammar_rule(self):
        for rule in self.rules:
            if rule.rule == self.user_input_tokens():
                return rule.rule_name
        raise Exception("Syntax Error")

    def create_ast_for_rule_1(self):
        return ASTEcho(ASTString(self.tokens["STRING"]))


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
