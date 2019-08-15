import re
import random

TOKENS =   [re.compile(r'(?P<VARIABLE>BACKPACK)'), re.compile(r'(?P<ASSIGNMENT>PACK_WITH)'),
            re.compile(r'(?P<IF_START>WALK_PATH_IF_SEE)'),  re.compile(r'(?P<ECHO>echo)'),
            re.compile(r'(?P<BOOLEAN>true|false)'), re.compile(r'(?P<MODULUS>\(\*\)\>)'), 
            re.compile(r'(?P<EQUALS>OvO)'), re.compile(r'(?P<NOT_EQUAL>XvX)'), 
            re.compile(r'(?P<INTEGER>[\d]+)'), re.compile(r'(?P<STRSTART><<)'), 
            re.compile(r'(?:<<)(?P<STRING_CONTENT>.+)(?:>>)'), re.compile(r'(?P<STRSTOP>>>)'), 
            re.compile(r'(?P<END>CAMP)'), re.compile(r'(?:BACKPACK:)(?P<VARIABLE_NAME>.+)')]

class Interpreter(object):
    def __init__(self, text):
        self.text = text

    def response(self):
        tokeniser = Tokeniser(self.text)
        parser = Parser(tokeniser.create_tokens())
        return self.visit_tree(self._get_ast_method(parser))

    def visit_tree(self, ast_output):
        if isinstance(ast_output, ASTEcho):
            return self.visit_ast_echo(ast_output)
        elif isinstance(ast_output, ASTConditional):
            return self.visit_ast_conditional(ast_output)
        elif isinstance(ast_output, ASTModulus):
            return self.visit_ast_modulus(ast_output)


    def visit_ast_echo(self, ast_echo_node):
        return "Forest says: " + ast_echo_node.expr.value

    def visit_ast_modulus(self, ast_modulus_node):
        result1 = ast_modulus_node.operand1.value
        result2 = ast_modulus_node.operand2.value
        result3 = result1%result2
        return result3

    def visit_ast_equals(self, ast_equals_node):
        return self.visit_ast_modulus(ast_equals_node.operand1) == ast_equals_node.operand2.value

    def visit_ast_conditional(self, ast_conditional_node):
        if self.visit_ast_equals(ast_conditional_node.expr_branch) == True:
            return self.visit_ast_echo(ast_conditional_node.then_branch)
        else:
            return False

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
        self.grammar_rule_4 = GrammarRule("rule_4",["IF_START", "INTEGER", "MODULUS", "INTEGER", "EQUALS", "INTEGER", "ECHO", "STRSTART", "STRING_CONTENT", "STRSTOP"] )
        self.grammar_rule_5 = GrammarRule("rule_5", ["INTEGER", "MODULUS", "INTEGER"] )
        self.rules = [self.grammar_rule_1, self.grammar_rule_2, self.grammar_rule_3, self.grammar_rule_4, self.grammar_rule_5]

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
        raise Exception("Syntax Error " + self.return_error_message())

    def create_ast_for_rule_1(self):
        user_input_string = self.get_token_by_key()
        return ASTEcho(ASTString(user_input_string))

    def create_ast_for_rule_3(self):
        str_token1 = self.tokens[0]
        str_token3 = self.tokens[2]
        return ASTEquals(ASTString(str_token1["STRING_CONTENT"]), ASTString(str_token3["STRING_CONTENT"]))

    def create_ast_for_rule_4(self):
        int_token1 = self.tokens[1]
        int_token2 = self.tokens[3]
        int_token3 = self.tokens[5]
        str_token1 = self.tokens[8]
        integer_operand1 = ASTInteger(int_token1["INTEGER"])
        integer_operand2 = ASTInteger(int_token2["INTEGER"])
        integer_operand3 = ASTInteger(int_token3["INTEGER"])
        string_operand = ASTString(str_token1["STRING_CONTENT"])
        modulus_operator = ASTModulus(integer_operand1, integer_operand2)
        expr_branch = ASTEquals(modulus_operator, integer_operand3)
        return ASTConditional(expr_branch, ASTEcho(string_operand), "Aleks")

    def create_ast_for_rule_5(self):
        int1 = self.tokens[0]
        int2 = self.tokens[2]
        int1_operand = ASTInteger(int1["INTEGER"])
        int2_operand = ASTInteger(int2["INTEGER"])
        modulus_op = ASTModulus(int1_operand, int2_operand)
        return modulus_op

    def get_token_by_key(self):
        for item in self.tokens:
            if "STRING_CONTENT" in item:
                return item["STRING_CONTENT"]

    def return_error_message(self):
        ERROR_MESSAGES = ["ERROR ʕノ•ᴥ•ʔノ ︵ =❱❯❭> =❱❯❭>", "Looks like you got lost in the Syntax Woods, Ranger ʕ·ᴥ·ʔ", "Forest does not know what this means ʅʕ•ᴥ•ʔʃ", "ERROR 🌲🌲🌲 ʕ·ᴥ·ʔ 🌲🌲🌲 YIKES", "٩ʕ•͡×•ʔ۶ This operation cant be completed", "Looks like you dont know Forest... but we dont know it either ⊂（´㉨｀*）⊃"]

        return random.choice(ERROR_MESSAGES)

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
        self.value = int(value)

def main():
    while True:
        text = input('=❱❯❭> ')
        interpreter = Interpreter(text)
        try:
            result = interpreter.response()
            print(result)
        except Exception as syntax_err:
            print("Oops!", syntax_err)


if __name__ == '__main__':
    main()