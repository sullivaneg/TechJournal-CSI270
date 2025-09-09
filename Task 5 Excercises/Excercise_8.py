# “Gather and Display Data”, your application should ask the user to insert the sales amount in dollars for every year
# starting from “Beginning Year” to “End Year”. These values should be printed in a tabular form (use \t), each year
# on a line. In addition, your application should calculate and print the average of these sales.

# Calculations
def average_sales(sales):
    """
    This function takes a list of sales and returns the average sale price over the entire time period.
    :param sales:
    :return: average
    """
    sum_sales = 0
    year_count = 0
    for sale in sales:
        sum_sales += sale
        year_count += 1
    average = sum_sales / year_count
    return average

def gen_year_list(start, end):
    """
    This function generates a list of years between start and end
    :param start:
    :param end:
    :return:
    """
    year_list = []
    year = start
    while year <= end:
        year_list.append(year)
        year += 1
    return year_list

def start_year_usr():
    """
    This function gets input from the user for the start year and validates input.
    :return: start year
    """
    while True:
        start_year = input("Enter the Beginning year: ")
        if len(start_year) < 4:
            print("Invalid year")
            continue
        else:
            try:
                start_year = int(start_year)
                break
            except ValueError:
                print("Please enter a valid year.")
                continue
    return start_year

def end_year_usr(start_year):
    """
    This function gets input from the user for the end year and validates input.
        :return: end year
        """
    while True:
        end_year = input("Enter the End year: ")
        if len(end_year) < 4:
            print("Invalid year")
            continue
        else:
            try:
                end_year = int(end_year)
                if end_year <= start_year:
                    print("End year can't be greater than or equal to start year.")
                    continue
                else:
                    break
            except ValueError:
                print("Please enter a valid year.")
                continue
    return end_year

def get_sales(start_year, end_year, year_list):
    """
    This function gets user input for the sales for each year and validates input.
    :param start_year:
    :param end_year:
    :param year_list:
    :return: sales_listf
    """
    print("Please enter the sales for years " + str(start_year) + "-" + str(end_year))
    sales_list = []
    for year in year_list:
        while True:
            sale = input("Year " + str(year) + ": ")
            try:
                sale = int(sale)
                break
            except ValueError:
                print("Please enter a valid number.")
                continue
        sales_list.append(sale)
    return sales_list



def main():
    print("Welcome to the Sales Calculator!\n_____________________________________")
    start_year = start_year_usr()
    end_year = end_year_usr(start_year)
    year_list = gen_year_list(start_year, end_year)
    sales_list = get_sales(start_year, end_year, year_list)
    average = average_sales(sales_list)

    #print output
    print()
    print(f'Sales for years {start_year}-{end_year}:')
    print("______________________________________")

    for year, sale in zip(year_list,sales_list):
        print(f'Year {year}:\t {sale}')

    print("______________________________________")

    print(f'Average $ Sales for years {start_year}-{end_year}:\t {average}')

main()


