# 1.	Write a recursive method that displays the lyrics of the song “Bingo”.
# Write a complete demo program to test your recursive method.

def bingo(name):
    if len(name) == 0:
        print("The End")
    else:
        print("There was a farmer had a dog,")
        print("and Bingo was his name-O,")
        for i in range(3):
            print("-".join(name), end="!\n")
        print("And Bingo was his name-O!")
        bingo(name[1:])

bingo("BINGO")
