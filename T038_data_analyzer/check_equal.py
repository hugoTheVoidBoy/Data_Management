

def check_equal(description: str, actual, expected) -> bool:
    ''' A unit testing framework for ECOR1042 '''
    
    actual_type = type(actual)
    expected_type = type(expected)
    

    if actual_type != expected_type:
        
        print("{0} FAILED: expected ({1}) has type {2}, "
              "but actual ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '),
                      actual, str(actual_type).strip('<class> ')))
        return False
    if actual != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, actual))
        return False
    else:
        print("{0} PASSED".format(description))
        return True
        
    print("------")

