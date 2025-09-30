# 1. Define a function to print the number of minutes in seven weeks. Do not forget to give the function a suitable name.

def seven_week_min():
    """
    This function prints the number of minutes in 7 weeks.
    :return:
    """
    day_min = 60 * 24
    week_min = 7 * day_min
    sev_week_min = 7 * week_min
    print(f'The number of minutes in 7 weeks is: {sev_week_min}')
print('_______________________________________\nExercise #1: Seven Week Function\n_____________________________________'
      '__')
seven_week_min()