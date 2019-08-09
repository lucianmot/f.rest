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

    def isecho(self):
        if bool(re.match("echo", self.text)) == True:
            return True
        else:
            return False

    def tokenise_echo(self):
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
                raise Exception('Exception 7') 


    def create_token(self):
        if self.isecho() == True:
            return self.tokenise_echo()
        elif bool(re.search("true", self.text)) == True:
            return {"TRUE" : "true"}
        elif bool(re.search("false", self.text)) == True:
            return {"FALSE" : "false"}
        else:
            raise Exception("Error 3")


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
    