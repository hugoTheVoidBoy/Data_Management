# LucasHallam
# 101273089
# Ashley Tran
# 101262975

from T038_M1_load_data import student_school_dictionary
from T038_M1_load_data import student_ages_dictionary
from T038_M1_load_data import student_health_dictionary
from T038_M1_load_data import student_failures_dictionary
from T038_M1_load_data import add_average
import matplotlib.pyplot as plt
from scipy.optimize import fminbound
import numpy

def student_list(dictionary: dict) -> list[dict]:
    """ Returns the data from a dictionary in the form of a list. 

    Examples: 

    student_list(student_ages_dictionary("student-mat.csv"))
    >>> [{'School': 'GP', 'Studytime': 2, 'Failures': 3, 'Health': 3, 'Absences'
    : 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.33, 'Age': 15}, {'School': 'GP'
    , 'Studytime': 3, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 15, 'G2':
    14, 'G3': 15, 'G_Avg': 14.67, 'Age': 15}, {'School': 'GP', 'Studytime': 2, '
    Failures': 0, 'Health': 1, 'Absences': 0, 'G1': 16, 'G2': 18, 'G3': 19, 
    'G_Avg': 17.67, 'Age': 15}, {another element}, … ]
    """
    student_list = []
    for key in add_average(dictionary):
        for student in dictionary[key]:
            if "Age" not in list(student.keys()):
                student.update(Age=key)
            elif "School" not in list(student.keys()):
                student.update(School=key)
            elif "Health" not in list(student.keys()):
                student.update(Health=key)
            elif "Failures" not in list(student.keys()):
                student.update(Failures=key)
            student_list.append(student)
    return (student_list)

def curve_fit(dct: dict, attr: str, poly: int) -> list:
    """ Given desired dictionary and attributr
    Return equation of the best fit of the average Avg as a list of coefficients 
    Condition: 1 < poly < 5
    Example:
    >>> curve_fit(student_failures_dictionary("student-mat.csv"), 'G1', 2))
    array([ 3.16707595e-04,  1.01841382e+00, -5.26310477e-01])
    >>> curve_fit(student_failures_dictionary("student-mat.csv"), 'G2', 1))
    array([0.95122991, 0.55215556])

    """
    new_list = student_list(dct)
    attr_list=[]
    finalavg_list=[]
    
    list_x=[]
    list_y=[]
    z=0
    
    for value in new_list:
        
        value_attr = value[attr]        #run through the desired attribute in the dictionary   
        if value_attr not in attr_list:         #if it is not put together into a list yet
            attr_list.append(value_attr)            #then we put them
    list_x = attr_list                                  #they are our X list
    
    for i in attr_list:                 #with each attribute in the list
        avg_list=[]                     #list of Avg that come with the same attr
        count_avg= 0                       #refresh this every time we calculate Y for each X
        y = 0                              #refresh this every time we calculate Y for each X 
        
        for value in new_list:              #run through the desired attribute in the dictionary
            value_attr = value[attr]        
            if value_attr == i:             #Those with the same attr data
                value_avg = value['G_Avg']      #Take their G_Avg
                avg_list.append(value_avg)      #put them into the avg_list
                count_avg += 1                  #count them
        y = sum(avg_list) / count_avg        #Take their average G_Avg, this is the Y for the attr
         
        list_y.append(y)                        #Loop the process above, we got a list of Ys
    
    if len(list_x) > (poly):                    #Plot the equation
        z = poly
    else:
        z = len(list_x)-1

    coef = numpy.polyfit(list_x, list_y, z)
    interval = [min(list_x), max(list_x)]
    
    return coef, interval

def maximum(dictionary: dict, attribute: str) -> tuple:
    """
    Returns a tuple containing the x and y value of the local maximun between 
    the lowest and the highest value of the attribute.
    
    Example:
    >>> maximum("Age")
    (age, grade)
    """
    global coef
    coef, x_points = curve_fit(dictionary, attribute, 2)
    x_max = fminbound(max_curve_function, x_points[0], x_points[1])
    y_max = curve_function(coef, x_max)    
    return (x_max, y_max)

def max_curve_function(x):
    global coef
    return -curve_function(coef, x)

def curve_function(coef_list: list[float], x: float):
    """Return a polynomial based on the coefficients from coef_list
    Precondition: (coef_list) > 0
    """
    global coef
    curve_result = ((coef[0]) * x ** 2) + (coef[1] * x) + coef[2]
    return curve_result



def curve_fit2(dct: dict, attr: str, degree: int):
    """ Given desired dictionary and attributr
    Return equation of the best fit of the average Avg as a list of coefficients 
    Condition: 1 < poly < 5
    Example:
    >>> curve_fit(student_failures_dictionary("student-mat.csv"), 'G1', 2))
    array([ 3.16707595e-04,  1.01841382e+00, -5.26310477e-01])
    >>> curve_fit(student_failures_dictionary("student-mat.csv"), 'G2', 1))
    array([0.95122991, 0.55215556])

    """
    new_list = student_list(dct)
    attr_list = []
    finalavg_list = []

    list_x = []
    list_y = []
    z = 0

    for value in new_list:

        # run through the desired attribute in the dictionary
        value_attr = value[attr]
        if value_attr not in attr_list:  # if it is not put together into a list yet
            attr_list.append(value_attr)  # then we put them
    list_x = attr_list  # they are our X list

    for i in attr_list:  # with each attribute in the list
        avg_list = []  # list of Avg that come with the same attr
        count_avg = 0  # refresh this every time we calculate Y for each X
        y = 0  # refresh this every time we calculate Y for each X

        for value in new_list:  # run through the desired attribute in the dictionary
            value_attr = value[attr]
            if value_attr == i:  # Those with the same attr data
                value_avg = value['G_Avg']  # Take their G_Avg
                avg_list.append(value_avg)  # put them into the avg_list
                count_avg += 1  # count them
        # Take their average G_Avg, this is the Y for the attr
        y = sum(avg_list) / count_avg

        list_y.append(y)  # Loop the process above, we got a list of Ys

    if len(list_x) > (degree):  # Plot the equation
        z = degree
    else:
        z = len(list_x) - 1

    return ((numpy.polyfit(list_x, list_y, z)), list_x)



# A function that finds the y value for any given x
def find_y(x):
    """Returns the y value for any given x value, Given the X value.
    The function assumes that the curve_fit function has been called as it uses those values 
    """
    global coeff  # Sets the coeff variable to global to allow it to be used in other functions
    # Equation for quadratics to find the y-value
    y_value = ((coeff[0]) * x ** 2) + (coeff[1] * x) + coeff[2]
    return y_value

# Minimum function


def minimum(dictionary: dict, string: str) -> tuple:
    """Returns the local minimum point in tuple form (x,y), 
    Given a string that tells the function which x_values to use

    Example Call:

    >>> minimum ("Failures")
    (2.9999965472915386, 6.354604510301344)
    """
    global coeff
    # Adds G_Avg to the inputed dictionary
    final_dictionary = add_average(dictionary)
    # Unpacks the curve_fit call and the data it returns
    coeff, x_points = curve_fit2((final_dictionary), string, 2)
    x_points.sort()  # Sorts the list of x_points
    # Sets the min point to the first x point in the list
    x_min = x_points[0]
    # Sets the max point to the last x point in the list
    x_max = x_points[-1]
    # Calls the fminbound function
    x = fminbound(find_y, x_min, x_max)
    return (x, find_y(x))

# Main Script
if __name__ =='__main__':
    print(maximum(student_school_dictionary("student-mat.csv"), "Age"))
    print(maximum(student_school_dictionary("student-mat.csv"), "Health"))
    print(maximum(student_school_dictionary("student-mat.csv"), "Failures"))
    print(maximum(student_school_dictionary("student-mat.csv"), "StudyTime"))
    print(maximum(student_school_dictionary("student-mat.csv"), "Absences"))

    print(minimum (student_school_dictionary("student-mat.csv"), "Failures"))
    print(minimum (student_ages_dictionary("student-mat.csv"), "G_Avg"))
    print(minimum (student_health_dictionary("student-mat.csv"), "Failures"))
    print(minimum (student_failures_dictionary("student-mat.csv"), "G1"))