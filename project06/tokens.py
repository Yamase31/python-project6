"""
Author: Laurie Jones, Harry Pinkerton, James Lawson
File: tokens.py
Tokens for processing expressions.
"""

class Token(object):
    """Represents a word in the language."""

    UNKNOWN  = 0        # unknown

    PARO     = 2       # open parenthesis
    PARC     = 3       # closed parenthesis
    
    INT      = 4        # integer
    
    MINUS    = 5        # minus    operator
    PLUS     = 6        # plus     operator
    MUL      = 7        # multiply operator
    DIV      = 8        # divide   operator
    MOD      = 9        # modulo   operator
    EXP      = 10       # exponent operator


    FIRST_OP = 5        # first operator code

    def __init__(self, value):
        """Sets the type and the value, depending on
        the value argument (either an integer or a string)."""
        # If we're an integer then make an integer token
        if type(value) == int:
            self._type = Token.INT
        
        # Otherwise, make an non-int token
        else:
            self._type = self._makeType(value)
        
        # Value is either the int value or the string operand
        self._value = value

    def isOperator(self):
        """Returns True if the token is an operator,
        or False otherwise."""
        
        return self._type >= Token.FIRST_OP

    def getPrecedence(self):
        """Returns the precedence number of the operator."""

        if self._type == Token.EXP:
            return 2
        
        elif self._type in (Token.MUL, Token.DIV, Token.MOD):
            return 1
        
        elif self._type in (Token.PLUS, Token.MINUS):
            return 0
        
        else:
            return -1

    def __str__(self):
        """Returns the string rep of the token."""
        return str(self._value)
    
    def getType(self):
        """Returns the token's type."""
        return self._type
    
    def getValue(self):
        """Returns the token's value."""        
        return self._value

    def _makeType(self, string):
        """Returns the token's type, given its
        string value."""
        # Convert from a string to a Token.<type>
        if   string == '*': return Token.MUL
        elif string == '/': return Token.DIV
        elif string == '+': return Token.PLUS
        elif string == '-': return Token.MINUS
        elif string == '%': return Token.MOD
        elif string == '^': return Token.EXP
        elif string == '(': return Token.PARO
        elif string == ')': return Token.PARC
        else:               return Token.UNKNOWN

def main():
    """A simple tester program."""
    plus = Token("+")
    minus = Token("-")
    mul = Token("*")
    div = Token("/")
    mod = Token("%")
    exp = Token("^")
    unknown = Token("#")
    anInt = Token(34)
    print(plus, minus, mul, div, mod, exp, unknown, anInt)

if __name__ == '__main__': 
    main()

