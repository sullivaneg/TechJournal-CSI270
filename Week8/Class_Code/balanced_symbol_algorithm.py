from all_classes import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


print(parChecker('[{()]'))
print(parChecker('([(()){}((()))])'))
print(parChecker('((())((())))'))
#print(parChecker('(3*4)+(5*6)*[(8*7)/2)]))')) Returns an error
print(parChecker("[()]{}{[()()]())}"))
