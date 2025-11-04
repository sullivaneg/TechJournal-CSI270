# Write code that prints all the numbers up to 41 that are not divisiable by either of these factors =
# [2, 3, 5, 7]
# When done, attempt doing it using a generator. You can use count() if you wish.

factors = [2, 3, 5, 7]
# _________My code__________

num_list = [n for n in range(42) if all(n % f != 0 for f in factors)]
print("______List Comp______")
print(num_list)

G = (n for n in range(42) if all(n % f != 0 for f in factors))
print("______Generator______")
print(G) #Checking that it's a generator object

# __________________________

for val in G:
    print(val, end = ' ')
    if val > 40: break

# Goal Result : 1 11 13 17 19 23 29 31 37 41