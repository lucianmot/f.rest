import re

class Interpreter(object):
    def __init__(self, text):
        self.text = text

    def response(self):
        tokeniser = Tokeniser(self.text)
        token = tokeniser.create_token()
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
        self.tokenoutput = []

    
    # our input will be echo << Hello World! >>
    # split everything by space in an array
     # have individual element as a string in an array
    # iterate over each element
    def tokeniser2(self):
        TOKEN_TYPES = [ {"ECHO" : "echo"}, {"STRSTART" : "<<"}, {"STRING" : "string"} , { "STREND" : ">>"} ]
        tech = "echo << Hello World! >>"
        split_text = tech.split()
        for element in split_text:
            for token_type in TOKEN_TYPES:
                if element == token_type["ECHO"]:
                    self.tokenoutput.append(token_type)
        
    # match each element to a token type from a token array/dict
    # once it detects << it would save the index on var str start
    # the attempt to search for >> save its index on var str end
    # loop taking in str start index and str end index
    # everything that is between those 2 index would become a joined string
    # expect to see an array called tokenized_output = [{"ECHO" : "echo", "STRSTART" : "<<", "STRING" : "Hello World", "STRSTOP" : ">>"]
    

    def create_token(self):
        if bool(re.match("echo", self.text)) == True:
            echo = self.text[0:4]
            restofstr = self.text[4:]
            if bool(re.match("<<", restofstr)) == False:
                raise Exception("Error 1")
            elif bool(re.match("<<", restofstr)) == True:
                if bool(re.search(">>", restofstr)) == False:
                    raise Exception("Error 2")
                elif bool(re.search(">>", restofstr)) == True:
                    strstart = restofstr[0:2]
                    middle = restofstr[2:-2]
                    strstop = restofstr[-2:]
                    return {"ECHO": echo, "STRSTART" : strstart, "STRING" : middle, "STRSTOP" : strstop}

        else:
            raise Exception("Error 3")


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
