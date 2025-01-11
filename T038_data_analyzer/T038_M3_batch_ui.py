# HugoNgo
# Amber Boies
# LucasHallam
# Ashley Tran

from T038_M2_sort_plot import sort_students_selection
from T038_M2_sort_plot import student_list
import matplotlib.pyplot as plt
import numpy
from T038_M2_sort_plot import histogram
from T038_M3_optimization import minimum
from T038_M3_optimization import maximum
from T038_M1_load_data import add_average
from T038_M1_load_data import load_data as ld

def batch_ui():
    """Create a batch UI that read every line in a text file and run as command
    Example: >>>Please enter the name of the file where your commands are stored: test.txt
    Data Loaded
    Data is loaded from student-mat.csv for Age

    The best value for the attribute Age is 15
    The worst value for the attribute Health is 4
    << Histogram of  StudyTime will be displayed>>
    << Histogram of  Failures will be displayed>>
    Invalid command.
    Program will be terminated"""
    
    command = ()
    
    filename= input('Please enter the name of the file where your commands are stored: ')
    infile = open(filename, "r")
    
    for line in infile:
        
        item = line.strip().split(";")

        input_command = item[0]
        if input_command.upper() == 'L':
            user_input_filename = item[1]
            user_input_attribute = item[2]
            print('Data Loaded')
            loaded_data = add_average(
                (ld(str(user_input_filename), str(user_input_attribute))))

        elif input_command.upper() == 'S':
            if loaded_data == None:
                print('File not loaded. Please, load a file first')

            else:
                user_input_sorting_attribute = item[1]
                user_yes_no = item[2]
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
                user_input_histogram_attribute = item[1]
                print("<< Histogram of ", item[1], "will be displayed>>")
                result = histogram(
                        loaded_data, user_input_histogram_attribute)


        elif input_command.upper() == 'W':
            if loaded_data == None:
                print('File not loaded. Please, load a file first')

            else:
                user_input_worst_attribute = item[1]
                worst_value = minimum(loaded_data, user_input_worst_attribute)

                print(("The worst value for the attribute " + str(user_input_worst_attribute) +
                      " is " + str(round((worst_value[0])))))

        elif input_command.upper() == 'B':
            if loaded_data == None:
                print('File not loaded. Please, load a file first')

            else:
                user_input_best_attribute = item[1]
                best_value = maximum(loaded_data, user_input_best_attribute)

                print(("The best value for the attribute " + str(user_input_best_attribute) +
                      " is " + str(round((best_value[0])))))

        elif input_command.upper() == 'Q':
            print('Program will be terminated')
            break

        else:
            print('Invalid command.')
    infile.close()
    
#Main function
if __name__ =='__main__':
    batch_ui()
