import re

class Interpreter(object):
    def __init__(self, text):
        self.text = text

    def response(self):
        tokeniser = Tokeniser(self.text)
        token = tokeniser.create_token()
        return token.get("STRING")


class Tokeniser(object):
    def __init__(self, text):
        self.text = text

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


class GrammarRule(object):
    def __init__(self, rule_name, rule):
        self.rule_name = rule_name
        self.rule = rule
