#6. Write a program to compute the yearly increase for three employees’ salary as follow:
#           If the number of working years is more than 10, then the increase is 10 plus the current salary.
#           if the number of working years is 10 then the increase is 7 plus the current salary.
#           Else, the increase is 3 plus the current salary.
# The salary and number of current working years should be entered by the user.

def employee_name():
    flag = False
    while not flag:
        name = input("Enter Employee's name: ")
        if len(name) < 1:
            print("Length Insufficient: Please enter a name")
            flag = False
        else:
            # For first and last names
            name_nospace = name.replace(" ", "")
            flag = name_nospace.isalpha()
    return name

def work_years():
    """
    This function takes user input for work years, does error handling and returns an integer.
    :return: work_years
    """
    while True:
        years = input("Working Years: ")
        try:
            years = int(years)
            break

        except ValueError:
            print("Please enter a number")
            continue
    return years

def current_salary():
    """
    This function takes user input for current salary, does error handling and returns an integer.
    :return: current_salary
    """
    while True:
        salary = input("Current Salary: ")
        try:
            salary = float(salary)
            break

        except ValueError:
            print("Please enter a valid salary")
            continue

    return salary

def new_salary(salary, years):
    """
    This function takes the years worked and the current salary and computes the new salary.
    :return: new_salary
    """
    if years > 10:
        salary_new = (2 * salary) + 10
    elif years == 10:
        salary_new = (2 * salary) + 7
    else:
        salary_new = (2* salary) + 3
    return salary_new

def main():
    employee_raises = {}
    for i in range(3):
        name = employee_name()
        years = work_years()
        salary = current_salary()
        salary_new = new_salary(salary, years)
        employee_raises[name] = salary_new

    print("\nEmployee Raises:\n_________________________")
    for name, salary in employee_raises.items():
        print(f"{name}: {salary}")

main()

