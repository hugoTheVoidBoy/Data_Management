# Hugo Ngo
# Ashley Tran
# Amber Boies
# Lucas Hallam

import matplotlib.pyplot as plt
import numpy
from T038_M1_load_data import student_school_dictionary
from T038_M1_load_data import student_health_dictionary
from T038_M1_load_data import student_ages_dictionary
from T038_M1_load_data import student_failures_dictionary
from T038_M1_load_data import add_average
from typing import Dict,List


def student_list(dictionary: Dict) -> List[Dict]:
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


def sort_students_bubble(dictionary: Dict, string: str) -> List[Dict]:
    """Return a sorted list of dictionaries given the dictionary and a string,
    the string dictates what key the dictionary will be sorted by

    Example:
    >>> sort_students_bubble (student_ages_dictionary("student-mat.csv"), "G1")
    [{'School': 'BD', 'Studytime': 2, 'Failures': 1, 'Health': 5, 'Absences': 8, 'G1': 3, 'G2': 5, 'G3': 5, 'G_Avg': 4.33, 'Age': 18}, ...] 
    """

    # This checks what the string equals
    if string == "Age":
        # Assigns the array variable to the student list
        arr = student_list(dictionary)
        swap = True
        while swap:
            swap = False
            for i in range(len(arr) - 1):
                if (arr[i]).get("Age") > (arr[i + 1]).get("Age"):
                    # swaps the values
                    aux = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = aux
                    swap = True

# This same process is repeated depending on what the string is

    elif string == "Health":
        arr = student_list(dictionary)
        swap = True
        while swap:
            swap = False
            for i in range(len(arr) - 1):
                if (arr[i]).get("Health") > (arr[i + 1]).get("Health"):
                    # swap
                    aux = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = aux
                    swap = True

    elif string == "StudyTime":
        arr = student_list(dictionary)
        swap = True
        while swap:
            swap = False
            for i in range(len(arr) - 1):
                if (arr[i]).get("StudyTime") > (arr[i + 1]).get("StudyTime"):
                    # swap
                    aux = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = aux
                    swap = True

    elif string == "Failures":
        arr = student_list(dictionary)
        swap = True
        while swap:
            swap = False
            for i in range(len(arr) - 1):
                if (arr[i]).get("Failures") > (arr[i + 1]).get("Failures"):
                    # swap
                    aux = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = aux
                    swap = True

    elif string == "Absences":
        arr = student_list(dictionary)
        swap = True
        while swap:
            swap = False
            for i in range(len(arr) - 1):
                if (arr[i]).get("Absences") > (arr[i + 1]).get("Absences"):
                    # swap
                    aux = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = aux
                    swap = True

    elif string == "G1":
        arr = student_list(dictionary)
        swap = True
        while swap:
            swap = False
            for i in range(len(arr) - 1):
                if (arr[i]).get("G1") > (arr[i + 1]).get("G1"):
                    # swap
                    aux = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = aux
                    swap = True

    elif string == "G2":
        arr = student_list(dictionary)
        swap = True
        while swap:
            swap = False
            for i in range(len(arr) - 1):
                if (arr[i]).get("G2") > (arr[i + 1]).get("G2"):
                    # swap
                    aux = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = aux
                    swap = True

    elif string == "G3":
        arr = student_list(dictionary)
        swap = True
        while swap:
            swap = False
            for i in range(len(arr) - 1):
                if (arr[i]).get("G3") > (arr[i + 1]).get("G3"):
                    # swap
                    aux = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = aux
                    swap = True

    elif string == "G_Avg":
        arr = student_list(dictionary)
        swap = True
        while swap:
            swap = False
            for i in range(len(arr) - 1):
                if (arr[i]).get("G_Avg") > (arr[i + 1]).get("G_Avg"):
                    # swap
                    aux = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = aux
                    swap = True

    elif string == "School":
        arr = student_list(dictionary)
        swap = True
        while swap:
            swap = False
            for i in range(len(arr) - 1):
                if (arr[i]).get("School") > (arr[i + 1]).get("School"):
                    # swap
                    aux = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = aux
                    swap = True

    return arr


def sort_students_selection(dictionary: Dict, attribute: str) -> List[Dict]:
    """ Returns the dictionary passed to the function sorted by the indicated
    attribute which could be any of the keys listed in the dictionary. All 
    attributes will be sorted in ascending numerical order except for "School" 
    which will be sorted in ascending alphbetical order. 

    Preconditions: The attribute must be present in the dictionary 

    Examples: 
    sort_students_selection((student_ages_dictionary("student-mat.csv")), "G1")
    >>> [{'School': 'BD', 'Studytime': 2, 'Failures': 1, 'Health': 5, 'Absences'
    : 8, 'G1': 3, 'G2': 5, 'G3': 5, 'G_Avg': 4.33, 'Age': 18}, {'Scho ol': 'MB', 
    'Studytime': 1, 'Failures': 2, 'Health': 5, 'Absences': 0, 'G1': 4, 'G2': 0,
    'G3': 0, 'G_Avg': 1.33, 'Age': 16}, {'School': 'CF', 'Studytime': 2,
    'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7, 
    'G_Avg': 7.0, 'Age': 15}, {'School': 'MB', 'Studytime': 2, 'Failures': 0, 
    'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5, 'G_Avg': 5.0, 'Age': 
    16}, {'School': 'GP', 'Studytime': 2, 'Failures': 0, 'Health': 3, 'Absences'
    : 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33, 'Age': 17}, {another element}
    , … ]
    """
    # Sorts the data from the dictionary using student_list function and assigns it to selection
    selection = student_list(dictionary)

    for i in range(len(selection)):  # Iterates through all the elements in selection
        min_index = i
        # Finding the index of the minimum element in the rest of the unsorted array
        for j in range(i + 1, len(selection)):
            # Compares the value at the index at i for the given attribute and the value to right of index i
            if selection[j][attribute] < selection[min_index][attribute]:
                min_index = j  # if the value at the index to the right of i is less then it will become the new minimum index
        # Swaps the found minimum element with the element in position i
        selection[i], selection[min_index] = selection[min_index], selection[i]
    return selection  # returns the soreted dictionary by the attribute

def curve_fit(dct: Dict, attr : str, poly: int) -> List:
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
        y = sum(avg_list)/count_avg             #Take their average G_Avg, this is the Y for the attr
        
        
        
        list_y.append(y)                        #Loop the process above, we got a list of Ys
    
    
    if len(list_x) > (poly):                    #Plot the equation
        z = poly
    else:
        z = len(list_x)-1
       
    return (numpy.polyfit(list_x, list_y, z))

def histogram(dictionary: Dict, string: str) -> None:
    """
    Preconditions: 
    "string" is an attribute. (eg. School, Health, Age, etc.)
    
    Return None and show a histogram of the number of students at each level of 
    the attribute.
    
    Example:
    Health -> 1:47, 2:45, 3:91, 4:66, 5: 146
    """
    lst = student_list(dictionary) #put student data in a list
    h = {}
    for elem in lst: #for each dict in the list
        if elem[string] in h:
            h[elem[string]] = 1 + h[elem[string]] #add 1 to num of students
        else:
            h[elem[string]] = 1 #add the key with value of 1 if not in the dict yet

    x_list = h.keys()
    y_list = h.values()
    
    fig = plt.figure() # Create a figure
    plt.title("Histogram") # Add a title to the figure
    plt.xlabel(string) # Labeling the axis
    plt.ylabel('Number of Students')
    plt.bar(x_list, y_list, color='teal') # Data
    plt.show() # Showing the figure
    
if __name__ == "__main__":    #MainScript only run directly
    
    student_list(student_ages_dictionary("student-mat.csv"))
    student_list(student_health_dictionary("student-mat.csv"))
    student_list(student_school_dictionary("student-mat.csv"))
    student_list(student_failures_dictionary("student-mat.csv"))


    sort_students_bubble(student_ages_dictionary("student-mat.csv"), "G1")
    sort_students_bubble(student_health_dictionary("student-mat.csv"), "G_Avg")
    sort_students_bubble(student_school_dictionary("student-mat.csv"), "Failures")
    sort_students_bubble(student_failures_dictionary("student-mat.csv"), "StudyTime")
    
    sort_students_selection((student_ages_dictionary("student-mat.csv")), "G1")
    sort_students_selection((student_ages_dictionary("student-mat.csv")), "StudyTime")
    sort_students_selection((student_health_dictionary("student-mat.csv")), "School")
    sort_students_selection((student_failures_dictionary("student-mat.csv")), "Failures")
    sort_students_selection((student_school_dictionary("student-mat.csv")), "G_Avg")

    histogram(student_school_dictionary("student-mat.csv"), "Age")
    histogram(student_health_dictionary("student-mat.csv"), "School")
    histogram(student_ages_dictionary("student-mat.csv"), "Health")
    histogram(student_failures_dictionary("student-mat.csv"), "Failures")
    histogram(student_school_dictionary("student-mat.csv"), "StudyTime")
    histogram(student_health_dictionary("student-mat.csv"), "G1")
    histogram(student_ages_dictionary("student-mat.csv"), "G2")
    histogram(student_failures_dictionary("student-mat.csv"), "G3")
    histogram(student_school_dictionary("student-mat.csv"), "G_Avg")

    (curve_fit(student_failures_dictionary("student-mat.csv"), 'Failures', 5))
    (curve_fit(student_school_dictionary("student-mat.csv"), 'Health', 2))
    (curve_fit(student_ages_dictionary("student-mat.csv"), 'Age', 3))
    (curve_fit(student_ages_dictionary("student-mat.csv"), 'StudyTime', 4))
    (curve_fit(student_failures_dictionary("student-mat.csv"), 'Absences', 5))
    (curve_fit(student_failures_dictionary("student-mat.csv"), 'G1', 2))
    (curve_fit(student_failures_dictionary("student-mat.csv"), 'G2', 1))
    (curve_fit(student_school_dictionary("student-mat.csv"), 'G3', 2))
    (curve_fit(student_ages_dictionary("student-mat.csv"), 'G_Avg', 3))