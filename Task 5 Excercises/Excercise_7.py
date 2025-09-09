# “Calculate Deprecated Value”, your application should read the price of a car and display the value after the number
# of years in a list view. Each year the value is decremented by 5% of its actual price. The user should enter the
# number of years.


# car_name
flag = False
while not flag:
    car_name = input("Enter Car Make and Model: ")
    if len(car_name) < 1:
        print("Length Insufficient: Please enter a name")
        flag = False
    else:
        name_nospace = car_name.replace(" ", "")
        flag = name_nospace.isalpha()

#car price
while True:
    car_price = input(f'Enter the price of your {car_name} ')
    try:
        car_price = float(car_price)
        break

    except ValueError:
        print("Please enter a number")
        continue

# The number of years the user want's to see depreciated
while True:
    num = input("How many years of depreciation would you like to calculate? ")
    try:
        num = int(num)
        break

    except ValueError:
        print("Please enter a valid number")
        continue

depreciation = [(0.05 * i) * car_price for i in range(num)]
prices = [car_price - price for price in depreciation]

print(f'Yearly Depreciation Breakdown for {car_name}. Original price: {car_price}\n____________________'
      f'_________________________________')
for price in prices:
    print(f'Price after Year {prices.index(price)}: {price}')
