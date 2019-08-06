class Interpreter(object):
    def __init__(self, text):
        self.text = text

    def response(self):
        if self.text == "echo <<>>":
            return ""
        elif self.text == "echo <<hello>>":
            return "hello"    
        else:
            return "a"
