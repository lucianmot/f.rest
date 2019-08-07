#ECHO, LETTER, STRINGTXT, EOF, STRINGSTART, STRINGEND = 'ECHO', 'LETTER', 'STRINGTXT', 'EOF', 'STRINGSTART', 'STRINGEND'

class Interpreter(object):
    def __init__(self, text):
        self.text = text

    def response(self):
        token = self.tokeniser()[0]
        return token.get("STRING")

    def tokeniser(self):
        if self.text[0].isalpha() == True:
            return [{"STRING" : self.text[0]}]
        else:
            raise Exception
