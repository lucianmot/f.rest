import re

TOKENS =    [re.compile(r'(?P<ECHO>echo)'), re.compile(r'(?P<BOOLEAN>true|false)'), re.compile(r'(?P<INTEGER>\d)'),
            re.compile(r'(?P<WHITESPACE>\s)'), re.compile(r'(?P<STRSTART><<)'), re.compile(r'(?P<STRSTOP>>>)'),
            re.compile(r'(?:<<)(?P<STRING_CONTENT>.+)(?:>>)')]

class Interpreter(object):
    def __init__(self, text):
        self.text = text

    def response(self):
        tokeniser = Tokeniser(self.text)
        tokens = tokeniser.create_tokens()
        for token in tokens:
            if token.get('STRING_CONTENT') != None:
                return token.get('STRING_CONTENT')


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
        self.parse_dict = [["ECHO", "STRSTART", "STRING", "STRSTOP"]]

    def keytify_tokens(self):
        parse_keys = []
        for key in self.tokens:
            parse_keys.append(key)
            
        return parse_keys

    def run_parser(self):
        return self.parse_dict[0] == self.keytify_tokens()
    