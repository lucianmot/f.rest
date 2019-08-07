#ECHO, LETTER, STRINGTXT, EOF, STRINGSTART, STRINGEND = 'ECHO', 'LETTER', 'STRINGTXT', 'EOF', 'STRINGSTART', 'STRINGEND'
import re

class Interpreter(object):
    def __init__(self, text):
        self.text = text

    def response(self):
        token = self.tokeniser()[1]
        return token.get("STRING")

    def tokeniser(self):
        if bool(re.match("echo", self.text)) == True:
            echo = self.text[0:4]
            restofstr = self.text[5:]
            return [{"ECHO": echo},
                    {"STRING": restofstr}]
        else:
            raise Exception



# diffrent types of tokens
# input "ECHO a"; output [{ECHO: ECHO}, {STRING: a}]
# add parser as the next step
