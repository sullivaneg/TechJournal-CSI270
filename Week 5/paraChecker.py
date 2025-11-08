from Class_Code import stacks

# def paraChecker(symbolstring): #symbolstring will hold the pattern of '(', '[', '{', etc.
#     s = Stack()
#     math_symbols = '+, -, /, ^'
#     balanced = True #Determines if the string is balanced
#     index = 0
#     while index < len(symbolstring) and balanced:
#         symbol = symbolstring[index]
#         if symbol in '([{':
#             s.push(symbol)
#         else:
#             if s.is_empty():
#                 balanced = False
#             else:
#                 top = s.pop()
#                 if not matches(top,symbol):
#                     balanced = False
#                 else:
#                     pass
#         index = index + 1
#     if balanced and s.is_empty():
#         return True
#     else:
#         return False
#
# # Code below checks for balanced math equation symbols
#
# def matches(open, close):
#     opens = "([{" #{[( throws false because index is defined below
#     closes = ")]}"
#     return opens.index(open) == closes.index(close)
#
# print(paraChecker('()'))
# print(paraChecker('({})'))
# print(paraChecker('({[]{}})'))
# print(paraChecker('({}[])'))
# print(paraChecker('({)'))

def paraChecker(string):
    s = stacks.Stack()
    balanced = True
    index = 0
    while index < len(string) and balanced:
        char = string[index]
        if char == '(':
            s.push(char)
        elif char == ')':
            if s.is_empty():
                # If you don't have an opening parenthesis it can't be balanced
                balanced = False
            else:
                s.pop()
        index += 1
    return balanced and s.is_empty()


print(paraChecker('(())'))
print(paraChecker('(()'))