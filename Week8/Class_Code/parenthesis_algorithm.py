from all_classes import Stack

'''
Algorithm is successful detecting balanced '(', '[', '}, etc.
def paraChecker(symbolString): #symbolString will hold the pattern of '(', '[', '{ etc.
    s = Stack()
    balanced = True #Determines if the string is balanced
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
                else:
                    pass
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False
'''

#Code below checks for balance with math equation symbols
def paraChecker(symbolString): #symbolString will hold the pattern of '(', '[', '{ etc.
    s = Stack()
    math_symbols = '+, -, *, /, ^'
    balanced = True #Determines if the string is balanced
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        elif symbol in math_symbols or symbol.isdigit():
            pass
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
                else:
                    pass
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(open, close):
    opens = "{[("
    closes = "}])"
    return opens.index(open) == closes.index(close)

print(paraChecker('({1+5}+(6*7)^(2)/-2)'))




