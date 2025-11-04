from all_classes import Stack

'''
algorithm is successful detecting balanced '(', '[', '{'
def paraChecker(symbolstring): #symbolstring will hold the pattern of '(', '[', '{', etc.
    s = Stack()
    balanced = True #Determines if the string is balanced
    index = 0
    while index < len(symbolstring) and balanced:
        symbol = symbolstring[index]
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

def paraChecker(symbolstring): #symbolstring will hold the pattern of '(', '[', '{', etc.
    s = Stack()
    math_symbols = '+, -, /, ^'
    balanced = True #Determines if the string is balanced
    index = 0
    while index < len(symbolstring) and balanced:
        symbol = symbolstring[index]
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

# Code below checks for balanced math equation symbols

def matches(open, close):
    opens = "([{" #{[( throws false because index is defined below
    closes = ")]}"
    return opens.index(open) == closes.index(close)

print(paraChecker('()'))
print(paraChecker('({})'))
print(paraChecker('({[]{}})'))
print(paraChecker('({}[])'))
print(paraChecker('({)'))
