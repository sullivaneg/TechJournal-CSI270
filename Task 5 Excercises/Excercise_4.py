# Write a program that will read student grades (five grades) and add them to a list. Print the final list of student
# grades also, print the max and min grades in the list

# User Name
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

# Grades
grades = []
for i in range(1, 6):
    while True:
        grade = input(f'{i}. Enter your grade: ')
        try:
            grade = float(grade)

        except ValueError:
            print("Please enter a number")
            continue

        if grade < 0 or grade > 100:
            print("Please enter a valid number")
            continue

        else:
            break

    grades.append(grade)

#Printing grades
print()
print(f'{user_name}s Grades: {grades}')
print(f'{user_name}s Highest Grade: {max(grades)}')
print(f'{user_name}s Lowest Grade: {min(grades)}')



