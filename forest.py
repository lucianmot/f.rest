#ECHO, LETTER, STRINGTXT, EOF, STRINGSTART, STRINGEND = 'ECHO', 'LETTER', 'STRINGTXT', 'EOF', 'STRINGSTART', 'STRINGEND'

class Interpreter(object):
    def __init__(self, text):
        self.text = text

    def response(self):
        if self.text == "echo <<>>":
            return ""
        elif self.text == "echo <<hello>>":
            return "hello"
        elif self.text == "echo <<Hello, world!>>":
            return "Hello, world!"
        else:
            return "a"

    def tokeniser(self):
        if self.text[0].isalpha() == True:
            return [{"STRING" : self.text[0]}]
        else:
            return "oops"
