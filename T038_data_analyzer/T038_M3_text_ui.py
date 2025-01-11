# HugoNgo
# Amber Boies
# LucasHallam
# Ashley Tran

from T038_M1_load_data import load_data as ld
from T038_M1_load_data import add_average
from T038_M2_sort_plot import sort_students_selection
from T038_M2_sort_plot import student_list
import matplotlib.pyplot as plt
import numpy
from T038_M2_sort_plot import histogram
from scipy.optimize import fminbound
from T038_M3_optimization import maximum
from T038_M3_optimization import minimum


def command() -> None:
    """Initalizing function that prints all commands that a user can execute as well as the output for all possible user inputs.

    Example: 
    command()
    >>>  The available commands are:
                1. L) oad Data
                2. S) ort Data
                'School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3', 'G_Avg'
                3. H) istogram
                'School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences'
                4. W) orst ______ for Grades
                'Age', 'StudyTime', 'Failures', 'Health', 'Absences'
                5. B) est ______ for Grades 
               'Age', 'StudyTime', 'Failures', 'Health', 'Absences'
                6. Q) uit

           Please type your command: 

    """
    loaded_data = None
    while True:
        print("\n The available commands are:")
        commands = {'L)': '\t1. L) oad Data',
                    'S)': '\t2. S) ort Data\n \t \'School\', \'Age\', \'StudyTime\', \'Failures\', \'Health\', \'Absences\', \'G1\', \'G2\', \'G3\', \'G_Avg\'',
                    'H)': '\t3. H) istogram\n \t \'School\', \'Age\', \'StudyTime\', \'Failures\', \'Health\', \'Absences\'',
                    'W)': '\t4. W) orst ______ for Grades\n \t \'Age\', \'StudyTime\', \'Failures\', \'Health\', \'Absences\'',
                    'B)': '\t5. B) est ______ for Grades \n \t \'Age\', \'StudyTime\', \'Failures\', \'Health\', \'Absences\'',
                    'Q)': '\t6. Q) uit'}

        for command in commands.values():
            print(command)

        input_command = input("\nPlease type your command: ")

        if input_command.upper() == 'L':
            user_input_filename = input('Please enter the name of the file:')
            user_input_attribute = input(
                'Please enter the attribute to use as key:')
            print('Data Loaded')
            loaded_data = add_average(
                (ld(str(user_input_filename), str(user_input_attribute))))

        elif input_command.upper() == 'S':
            if loaded_data == None:
                print('File not loaded. Please, load a file first')

            else:
                user_input_sorting_attribute = str(input(
                    'Please enter the attribute you want to use for sorting: \n\'School\', \'Age\', \'StudyTime\', \'Failures\', \'Health\', \'Absences\', \'G1\', \'G2\', \'G3\', \'G_Avg\'\n:'))
                user_yes_no = input(str(
                    'Data Sorted. Do you want to display the data?:\n'))
                if user_yes_no.upper() == "Y":
                    result = sort_students_selection(
                        loaded_data, user_input_sorting_attribute)
                    for elem in result:
                        print(elem)
                elif user_yes_no.upper() == "N":
                    print()

        elif input_command.upper() == 'H':
            if loaded_data == None:
                print('File not loaded. Please, load a file first')

            else:
                user_input_histogram_attribute = str(input(
                    'Please enter the attribute you want to use for sorting: \n\'School\', \'Age\', \'StudyTime\', \'Failures\', \'Health\', \'Absences\'\n:'))
                user_yes_no = input(str(
                    'Data Sorted. Do you want to display the data?:\n'))
                if user_yes_no.upper() == "Y":
                    result = histogram(
                        loaded_data, user_input_histogram_attribute)
                    

                elif user_yes_no.upper() == "N":
                    print()

        elif input_command.upper() == 'W':
            if loaded_data == None:
                print('File not loaded. Please, load a file first')

            else:
                user_input_worst_attribute = str(input(
                    'Please enter the attribute you want to calculate the worse value of the attribute for in terms of grades: \n\'Age\', \'StudyTime\', \'Failures\', \'Health\', \'Absences\'\n:'))
                worst_age = minimum(loaded_data, user_input_worst_attribute)
                print(("The worst value for the attribute " + str(user_input_worst_attribute) +
                      " is " + str(round(worst_age[0]))))

        elif input_command.upper() == 'B':
            if loaded_data == None:
                print('File not loaded. Please, load a file first')

            else:
                user_input_best_attribute = str(input(
                    'Please enter the attribute you want to calculate the best value of the attribute for in terms of grades: \n\'Age\', \'StudyTime\', \'Failures\', \'Health\', \'Absences\'\n:'))
                best_age = maximum(loaded_data, user_input_best_attribute)
                print(("The best value for the attribute " + str(user_input_best_attribute) +
                      " is " + str(round(best_age[0]))))

        elif input_command.upper() == 'Q':
            print('Program will be terminated')
            break

        else:
            print('Invalid command.')

if __name__ =='__main__':
    command()






