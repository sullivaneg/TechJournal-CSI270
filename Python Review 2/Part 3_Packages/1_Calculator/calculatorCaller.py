from calculator import *

num_a = float(input("Enter the first number: "))
num_b = float(input("Enter the second number: "))

print("______________________________\nCALCULATOR\n____________________________")
print(f'SUM = {addition(num_a, num_b)}')
print(f'PRODUCT = {multiplication(num_a, num_b)}')
print(f'SUBTRACTION = {subtraction(num_a, num_b)}')
print(f'DIVISION = {division(num_a, num_b)}')