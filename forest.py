#ECHO, LETTER, STRINGTXT, EOF, STRINGSTART, STRINGEND = 'ECHO', 'LETTER', 'STRINGTXT', 'EOF', 'STRINGSTART', 'STRINGEND'
import re

class Interpreter(object):
    def __init__(self, text):
        self.text = text

    def response(self):
        tokeniser = Tokeniser(self.text)
        token = tokeniser.create_token()[2]
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
                    return [{"ECHO": echo},
                            {"STRSTART" : strstart},
                            {"STRING" : middle},
                            {"STRSTOP" : strstop}]
        else:
            raise Exception("Error 3")





# diffrent types of tokens
# input "ECHO a"; output [{ECHO: ECHO}, {STRING: a}]
# add parser as the next step
