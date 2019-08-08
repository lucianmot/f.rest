import unittest

#The parser accepts token array
#Checks token keys against grammar rules
#Returns true is it's a valid sentence ??????
#Returns false if it not.

class TestParser(unittest.TestCase):
    def test_something(self):
        #Given that the parser gets one token (ECHO)
        #When parser is run
        #It returns true
        from forest import Parser
        tokens = {"ECHO": 1, "STRSTART" : 2, "STRING" : 3, "STRSTOP" : 4}
        parser = Parser(tokens)
        self.assertEqual(parser.run_parser(), True)
        