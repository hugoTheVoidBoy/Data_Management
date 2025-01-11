#Hugo Ngo
#Ashley Tran
#Amber Boies
#Lucas Hallam


import string
from typing import List
from check_equal import check_equal

# Ashley Tran
# 101262975
def student_school_dictionary(filename: str) -> dict[str, list[dict[str, int]]]: #Function1
    """
    Return dictornary with the school initials as the key.
    
    Examples Output:
    { 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3,
      'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 }, {another element}, … ],
      'MB' : [ {'Age': 16, 'StudyTime': 2.6, 'Failures': 0, 'Health': 3,
      'Absences': 12, 'G1': 10, 'G2': 12, 'G3': 12 }, {another element}, … ], }

    """
    infile = open(filename, "r")

    #Variables
    school_initials = {}
    school_list = []
    gp_list = []
    mb_list = []
    cf_list = []
    bd_list = []
    ms_list = []

    firstline = True
    for line in infile:
        if firstline:    #skip first line
            firstline = False
            continue        

        line_as_list = line.strip().split(",") #splits each word in the line into items
        school_list.append(line_as_list[0]) #adds first word of the time into a list

        data_dictionary = {'Age': int(line_as_list[1]),
                           'StudyTime': int(line_as_list[2]),
                           'Failures': int(line_as_list[3]),
                           'Health': int(line_as_list[4]),
                           'Absences': int(line_as_list[5]),
                           'G1': int(line_as_list[6]),
                           'G2': int(line_as_list[7]),
                           'G3': int(line_as_list[8])}

        if line_as_list[0] == 'GP':
            gp_list.append(data_dictionary)
        elif line_as_list[0] == 'MB':
            mb_list.append(data_dictionary)
        elif line_as_list[0] == 'CF':
            cf_list.append(data_dictionary)
        elif line_as_list[0] == 'BD':
            bd_list.append(data_dictionary)
        elif line_as_list[0] == 'MS':
            ms_list.append(data_dictionary)
            
        school_initials = {'GP': gp_list,
                           'MB': mb_list,
                           'CF': cf_list,
                           'BD': bd_list,
                           'MS': ms_list}
    #print("{" + "\n".join("{!r}: {!r},".format(k, v)
                  #for k, v in school_initials.items()) + "}")
    infile.close()

    return (school_initials)

#AmberBoies
#101263889
def student_ages_dictionary(filename: str) -> dict:
    """ Prints multiple dictionaries with the key as the students age in the
    range of 15 to 22. Inside each of these dictionaries there is a list of 
    all students data with the same age as the key. 

    Example: 
    student_ages_dictionary('student-mat.csv') 
    >>>{ 15 : [ {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3,
                 'Health': 3, 'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10},
                {another element}, … ],
         16 : [ {'School': 'MS', 'StudyTime': 1, 'Failures': 1.2,
                 'Health': 4, 'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7},
                {another element}, … ], … } 
    """

    dict = {}
    age_list = []
    fifteen_list = []
    sixteen_list = []
    seventeen_list = []
    eighteen_list = []
    nineteen_list = []
    twenty_list = []
    twenty_one_list = []
    twenty_two_list = []

    infile = open(filename, "r")
    firstline = True
    for line in infile:
        if firstline:
            firstline = False
            continue

        line = line.strip().split(",")
        age_list.append(line[1])

        data_dictionary = {'School': str(line[0]),
                           'StudyTime': int(line[2]),
                           'Failures': int(line[3]),
                           'Health': int(line[4]),
                           'Absences': int(line[5]),
                           'G1': int(line[6]),
                           'G2': int(line[7]),
                           'G3': int(line[8])}

        age_dictionary = {15: fifteen_list,
                          16: sixteen_list,
                          17: seventeen_list,
                          18: eighteen_list,
                          19: nineteen_list,
                          20: twenty_list,
                          21: twenty_one_list,
                          22: twenty_two_list}

        if line[1] == '15':
            fifteen_list.append(data_dictionary)
        elif line[1] == '16':
            sixteen_list.append(data_dictionary)
        elif line[1] == '17':
            seventeen_list.append(data_dictionary)
        elif line[1] == '18':
            eighteen_list.append(data_dictionary)
        elif line[1] == '19':
            nineteen_list.append(data_dictionary)
        elif line[1] == '20':
            twenty_list.append(data_dictionary)
        elif line[1] == '21':
            twenty_one_list.append(data_dictionary)
        else:
            twenty_two_list.append(data_dictionary)

    #print("{" + "\n".join("{!r}: {!r},".format(k, v)
                          #for k, v in age_dictionary.items()) + "}")
    infile.close()
    return(age_dictionary)

# Lucas Hallam (#101273089)
def student_health_dictionary(filename: str) -> dict:  #Function3
    """Returns a dictionary which is made up of lists of dictionaries, 
    given data to be sorted. 

    Preconditions: Data must be sorted into catagories

    Examples: 
    >>> student_health_dictionary ('student-mat_notebook.txt')
    { 1: [ {'School': 'GP', 'Age': '17', 'StudyTime': '2', 'Failures': '0', 'Absences': '6', 'G1': '6', 'G2': '5', 'G3': '6'}, {another element}, ...]
    2: [another list of dictionaries] ...
    """

    health_list = []

    list_one = []
    list_two = []
    list_three = []
    list_four = []
    list_five = []
    dictionary = {}

    infile = open(filename, "r")

    firstline = True
    for line in infile:
        if firstline:
            firstline = False
            continue

        line = line.strip().split(",")
        health_list.append(line[4])

        data_dictionary = {'School': str(line[0]),
                           'Age': int(line[1]),
                           'StudyTime': int(line[2]),
                           'Failures': int(line[3]),
                           'Absences': int(line[5]),
                           'G1': int(line[6]),
                           'G2': int(line[7]),
                           'G3': int(line[8])}

        health_dictionary = {1: list_one,
                             2: list_two,
                             3: list_three,
                             4: list_four,
                             5: list_five}

        if line[4] == '5':
            list_five.append(data_dictionary)
        elif line[4] == '3':
            list_three.append(data_dictionary)
        elif line[4] == '4':
            list_four.append(data_dictionary)
        elif line[4] == '2':
            list_two.append(data_dictionary)
        else:
            list_one.append(data_dictionary)

    #print("{" + "\n".join("{!r}: {!r},".format(k, v)
          #for k, v in health_dictionary.items()) + "}")

    infile.close()
    return(health_dictionary)


#HugoNgo
#101281485
def student_failures_dictionary(filename: str) ->  dict: #Function4
    """
    Run through csv file to get data and print out the list of dictionary of failures from the students from 0 to 10.
    Precondition: csv file has to be in the same folder with this python file
    Example: >>>student_failures_dictionary("student-mat.csv")
    3: [{'School': 'GP', 'Age': '15', 'Studytime': '2', 'Failures': '3', 'Health': '3', 'Absences': '10', 'G1': '7', 'G2': '8', 'G3': '10'},]}
    """
    
    failure_initial = {}
    failure_list = []
    zero_list=[]
    one_list=[]
    two_list=[]
    three_list=[]
    four_list=[]
    five_list=[]
    six_list=[]
    seven_list=[]
    eight_list=[]
    nine_list=[]
    ten_list=[]
    
    infile = open(filename, "r")
    firstline = True
    for line in infile:
        if firstline:    #skip first line
            firstline = False
            continue        

        line_as_list = line.strip().split(",") #splits each word in the line into items
        failure_list.append(line_as_list[3]) #adds first word of the time into a list

        data_dictionary = {'School': str(line_as_list[0]),
                           'Age': int(line_as_list[1]),
                           'StudyTime': int(line_as_list[2]),
                           'Health': int(line_as_list[4]),
                           'Absences': int(line_as_list[5]),
                           'G1': int(line_as_list[6]),
                           'G2': int(line_as_list[7]),
                           'G3': int(line_as_list[8])}
        
        
        if line_as_list[3] == '0':
            zero_list.append(data_dictionary)
        elif line_as_list[3] == '1':
            one_list.append(data_dictionary)
        elif line_as_list[3] == '2':
            two_list.append(data_dictionary)
        elif line_as_list[3] == '3':
            three_list.append(data_dictionary) 
        elif line_as_list[3] == '4':
            four_list.append(data_dictionary)  
        elif line_as_list[3] == '5':
            five_list.append(data_dictionary)  
        elif line_as_list[3] == '6':
            six_list.append(data_dictionary)  
        elif line_as_list[3] == '7':
            seven_list.append(data_dictionary) 
        elif line_as_list[3] == '8':
            eight_list.append(data_dictionary)  
        elif line_as_list[3] == '9':
            nine_list.append(data_dictionary)  
        elif line_as_list[3] == '10':
            ten_list.append(data_dictionary)          

        failures_initial = { 0 : zero_list,
                             1 : one_list,
                             2 : two_list,
                             3 : three_list,
                             4 : four_list,
                             5 : five_list,
                             6 : six_list,
                             7 : seven_list,
                             8 : eight_list,
                             9 : nine_list,
                             10 : ten_list}  
    #print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in failures_initial.items()) + "}")
    infile.close()
    return(failures_initial)



def load_data(filechoice: str, choice: str) -> List[str]:
    
    if choice == "School":
        print("Data is loaded from",filechoice,"for",choice)
        returnfile = student_school_dictionary(filechoice)
        
    elif choice == "Age":
        print("Data is loaded from",filechoice,"for",choice)
        returnfile = student_ages_dictionary(filechoice)

    elif choice == "Health":
        print("Data is loaded from",filechoice,"for",choice)
        returnfile = student_health_dictionary(filechoice)
              
    elif choice == "Failures":
        print("Data is loaded from",filechoice,"for",choice, '\n')
        returnfile = student_failures_dictionary(filechoice)
    
    else: 
        returnfile = "Invalid Key"
    
    return(returnfile)        




def add_average(dict_name: dict) -> dict:
    """
    Add the average of the student’s grades (G1, G2 and G3) as an 
    additional attribute to the dictionary. Return the dictionary updated with 
    the average grade.
    
    Example output:
    { 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3,
             'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67 },
             {another element},
              … ],
      'MB' : [ {'Age': 16, 'StudyTime': 2.6, 'Failures': 0, 'Health': 3,
             'Absences': 12, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33 },
             {another element},
            … ],
       … }
    """
    new_list = []

    for lst in dict_name: # for every key in main dictionary
        for dct in dict_name[lst]: # for every inner dictionary in key's list
            a = dct['G1']
            b = dct['G2']
            c = dct['G3']
            d = round((a + b + c) / 3, 2)
            dct['G_Avg'] = d # adds averrage to inner dictionary
            new_list.append(dct) # append updated inner dictionary to new list
        dict_name[lst] = new_list
        new_list = []

    return (dict_name)




def create_list(dct):
    actual_keys = []
    for lst in dct: # for every key in the dictionary
        actual_keys.append(lst)

    return actual_keys

def test_1() -> None:               #TEST 1 - Ashley Tran
    keys1 = create_list(student_school_dictionary("student-mat.csv"))
    keys2 = create_list(student_health_dictionary("student-mat.csv"))
    keys3 = create_list(student_ages_dictionary("student-mat.csv"))
    keys4 = create_list(student_failures_dictionary("student-mat.csv"))

    failed = 0
    passed = 0
    
    a = check_equal('student_school_dictionary', keys1, ['GP', 'MB', 'CF', 'BD', 'MS'])
    b = check_equal('student_health_dictionary', keys2, [1, 2, 3, 4, 5])
    c = check_equal('student_ages_dictionary', keys3, [15, 16, 17, 18, 19, 20, 21, 22])
    d = check_equal('student_failures_dictionary', keys4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    for i in [a, c, b, d]:
        if i == True:
            passed += 1
        elif i == False:
            failed += 1
            
    print("Tests Passed:", passed)
    print("Tests Failed:", failed,'\n')
    


def test_2() -> None:                   #TEST 2 - LucasHallam
    """Tests all four dictionaries to make sure that they have the correct
    amount of data loaded

    Example Call (if all tests pass):
    >>>test_2()
    student_school_dictionary PASSED
    ------
    student_ages_dictionary PASSED
    ------
    student_health_dictionary PASSED
    ------
    student_failures_dictionary PASSED
    ------
    """

# Finds the amount of data in the file (i.e, how many students should be accounted for in each dictionary)
    count = 0
    infile = open("student-mat.csv", "r")
    for line in infile:
        count += 1
# Takes away the opening line (the keys)
    count -= 1

# Finds the total amount of students in the school dictionary
    school_list = ["GP", "MB", "CF", "BD", "MS"]
    school_final = 0
    for school_name in school_list:
        school_value = len((student_school_dictionary("student-mat.csv")[school_name]))
        school_final += school_value

# Finds the total amount of students in the age dictionary
    ages_list = [15, 16, 17, 18, 19, 20, 21, 22]
    ages_final = 0
    for age in ages_list:
        age_value = len((student_ages_dictionary("student-mat.csv")[age]))
        ages_final += age_value

# Finds the total amount of students in the health dictionary
    health_list = [1,2, 3, 4, 5]
    health_final = 0
    for health in health_list:
        health_value = len((student_health_dictionary("student-mat.csv")[health]))
        health_final += health_value

# Finds the total amount of students in the failures dictionary
    failures_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    failures_final = 0
    for failures in failures_list:
        failures_value = len((student_failures_dictionary("student-mat.csv")[failures]))
        failures_final += failures_value

# Compares the actual value to the expected value
    a = check_equal("student_school_dictionary", school_final, count)
    b = check_equal("student_ages_dictionary", ages_final, count)
    c = check_equal("student_health_dictionary", health_final, count)
    d = check_equal("student_failures_dictionary", failures_final, count)
    failed = 0
    passed = 0    
    for i in [a, c, b, d]:
        if i == True:
            passed += 1
        elif i == False:
            failed += 1
    print("Tests Passed:", passed)
    print("Tests Failed:", failed,'\n')
           
    return()

def test_3(filename: str) -> None:          #TEST 3 - Amber Boies
    """
    Tests that the individual student entries in each of the four
    dictionaries are stored correctly. Prints a description of the function
    being tested followed by PASSED or FAILED. PASSED indicates that the
    individual student entries are stored correctly and FAILED indicates that
    they are not. The amount of tests passed, failed, and completed will also
    print.  

    Examples: 
    test_3("student-mat.csv")
    >>>student_school_dictionary: PASSED
    >>>student_ages_dictionary: PASSED
    >>>student_failures_dictionary: PASSED
    >>>student_health_dictionary: PASSED
    >>>Tests Passed: 4
    >>>Tests Failed: 0
    >>>Test Completed: 4
    """

    # Expected values for each of the 4 dictionaries.

    health_headers = ['School', 'Age', 'StudyTime',
                      'Failures', 'Absences', 'G1', 'G2', 'G3']
    school_headers = ['Age', 'StudyTime', 'Failures',
                      'Health', 'Absences', 'G1', 'G2', 'G3']
    ages_headers = ['School', 'StudyTime', 'Failures',
                    'Health', 'Absences', 'G1', 'G2', 'G3']
    failures_headers = ['School', 'Age', 'StudyTime',
                        'Health', 'Absences', 'G1', 'G2', 'G3']

    # Importing all the required dictionaries.

    school_dict = load_data(filename, "School")
    ages_dict = load_data(filename, "Age")
    health_dict = load_data(filename, "Health")
    failures_dict = load_data(filename, "Failures")

   # Loading the data of a single student from each dictionary.

    school_student_data = school_dict["GP"][0]
    health_student_data = health_dict[1][0]
    ages_student_data = ages_dict[22][0]
    failures_student_data = failures_dict[2][0]

    # Creating a list containg the actual values for an individual student in each dictionary.

    actual_list_school = []
    for key in school_student_data.keys():
        actual_list_school.append(key)

    actual_list_health = []
    for key in health_student_data.keys():
        actual_list_health.append(key)

    actual_list_ages = []
    for key in ages_student_data.keys():
        actual_list_ages.append(key)

    actual_list_failures = []
    for key in failures_student_data.keys():
        actual_list_failures.append(key)

    failed = 0
    passed = 0

    test_one = check_equal("student_school_dictionary:",
                           actual_list_school, school_headers)

    test_two = check_equal("student_ages_dictionary:",
                           actual_list_ages, ages_headers)

    test_three = check_equal("student_failures_dictionary:",
                             actual_list_failures, failures_headers)

    test_four = check_equal("student_health_dictionary:",
                            actual_list_health, health_headers)

    counter = 0

    for i in [test_one, test_two, test_three, test_four]:
        if i == True:
            passed += 1
        elif i == False:
            failed += 1
        counter += 1

    print("Tests Passed:", passed)
    print("Tests Failed:", failed)
    print("Test Completed:", counter,'\n')
    

def test_4() -> str:                #TEST 4 - Hugo Ngo
    """ Check test pass when add_average is called:
    (1) The number of students in the dictionary does not change.
    (2) The G_Avg key is added to the student dictionary.
    (3) The value for G_Avg is properly calculated.
    
    Example: >>>test_4(student_school_dictionary("student-mat.csv"))
    Before and after G_Avg PASSED

    G_Avg is added to all dictionary PASSED

    Properly calculated G_Avg PASSED
    
    Test passed:  1
    Test failed:  0
    """
    dict_list = [student_school_dictionary("student-mat.csv"),student_ages_dictionary("student-mat.csv"),student_health_dictionary("student-mat.csv"),student_failures_dictionary("student-mat.csv")]
    test_pass=0
    test_fail= 0
    before_count = 0
    after_count = 0
    missing_count = 0
    correct_avg = 0
    total_test = 0
    
    for dict_name in dict_list:
        for key in dict_name:           #Count the value before calculating Avg
            for value in dict_name[key]:
                if True:
                    before_count += 1
                    
        x = add_average(dict_name)                       
        for key in x:                   #Count the value after calculating Avg 
            for value in x[key]:         
                if bool(value['G_Avg']):
                    after_count += 1
                    a = value['G1']
                    b = value['G2']
                    c = value['G3']
                    d = round((a + b + c) / 3, 2)  
                    if d == value['G_Avg']: #if G_Avg is correct
                        correct_avg +=1
                    else:print('Key #',key,' value #', value,' has a wrong G_Avg')
                   
                else:                   #Print out missing Avg key and value
                    print('Key #',key,' value #', value,' is missing G_Avg')
                    missing_count-=1  
    
            
        check1 = check_equal('Before and after G_Avg',before_count,after_count)       
        check2 = check_equal('G_Avg is added to all dictionary',missing_count,0)
        check3 = check_equal('Properly calculated G_Avg',correct_avg,after_count)
        total_test +=1
        if check1 == True and check2 == True and check3 == True:
            test_pass += 1
            print('-> Dictionary', total_test, 'PASSED\n')
        else:
            test_fail += 1
            print('-> Dictionary', total_test, 'FAILED\n')
    print('Test passed: ',test_pass)
    print('Test failed: ',test_fail, '\n')
    return()

#Main Script 
if __name__ == "__main__": 
    student_school_dictionary("student-mat.csv")
    student_ages_dictionary("student-mat.csv")
    student_health_dictionary("student-mat.csv")
    student_failures_dictionary("student-mat.csv")
    
    load_data("student-mat.csv", "School")
    load_data("student-mat.csv", "Age")
    load_data("student-mat.csv", "Health")
    load_data("student-mat.csv", "Failures")
    load_data("student-mat.csv", "NotCoolHomies")
    
    add_average(student_school_dictionary("student-mat.csv"))
    add_average(student_ages_dictionary("student-mat.csv"))
    add_average(student_health_dictionary("student-mat.csv"))
    add_average(student_failures_dictionary("student-mat.csv"))
    
    test_1()
    test_2()
    test_3("student-mat.csv")
    test_4()