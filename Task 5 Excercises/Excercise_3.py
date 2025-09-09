#Looking back on question 1, the system works only for one card! Modify your previous code to enable the user to
# specify the number of cards to purchase.

# Get the number of cards
while True:
    try:
        card_num = int(input("How many cards would you like? "))
        break
    except ValueError:
        print("Please enter a whole number. ")
        continue

# Get the card cost - I'm assuming the tax is the same for all of them
card_costs = []

for i in range(card_num):
    while True:
        try:
            card_cost = float(input("Enter the card cost: "))
            break
        except ValueError:
            print("Please enter a valid number. ")
            continue
    card_costs.append(card_cost)

while True:
    try:
        card_tax = float(input("Enter the card tax in the format 5% = 5: "))
        break
    except ValueError:
        print("Please enter a valid number. ")
        continue

# Total cost
def total_cost(card_cost):
    """
    This function calculates the total cost of all cards including taxes.
    :param card_cost:
    :return: total cost
    """
    return card_cost + (card_cost * (card_tax / 100))

# Results Screen
print()
print(f'YOUR CARD ORDER\n__________________________________________\n')
count = 1
cost_count = 00.00
for card_cost in card_costs:
    total = total_cost(card_cost)
    print(f'Card #{count}: ${card_cost} cost x %{card_tax} tax = ${total}')
    count += 1
    cost_count += total

print(f'Total cost: ${cost_count}')