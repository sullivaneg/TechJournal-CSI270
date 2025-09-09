# Task #5 Exercises

# 1. A program that is used for calculating the cost of prepaid recharge cards. For example, If the card cost is $5 and
# the card tax is 30%, then the final card cost is $6.5. Ask the user to enter his name and then read an integer from
# the user, which represents his/her birth year. Computes and displays the user’s name and age using the given
# birth year.

#Get users name and not accept numerical answers
flag = False
while not flag:
    user_name = input("Enter your name: ")
    if len(user_name) < 1:
        print("Length Insufficient: Please enter a name")
        flag = False
    else:
        # For first and last names
        user_name_nospace = user_name.replace(" ", "")
        flag = user_name_nospace.isalpha()

# Get users birth year and not accept strings

while True:
    birth_year = input("Enter your birth year: ")
    if len(birth_year) < 4:
        print("Invalid birth year")
        continue
    else:
        try:
            birth_year = int(birth_year)
            break
        except ValueError:
            print("Please enter a valid year.")
            continue

# Card calculations
while True:
    try:
        card_cost = float(input("Enter the card cost: "))
        break
    except ValueError:
        print("Please enter a valid number.")
        continue

while True:
    try:
        card_tax = float(input("Enter the card tax in the format 5% = 5: "))
        break
    except ValueError:
        print("Please enter a valid number.")
        continue

# Results Screen
print(f'Hi {user_name}! Born: {birth_year}')
print()
print(f'Card cost: ${card_cost}\nCard tax: {card_tax}%\n__________________________________________________________\n'
      f'TOTAL PRICE: {card_cost + (card_cost * (card_tax/100))}')








