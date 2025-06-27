###################################Floats#######################################
def isfloat:
    try:
        float(string)
        return True
    except ValueError:
        return False
 # # #  # # # # #  # # # # # # # # # # #  # # # # #  # # # #  # #
def inputFloat(message):
        while True:
            result=input(message)
            if isFloat(result):
                result=float(result)
                break
            else:
                print("please enter a valid float value!")
        return result
 # # #  # # # #  # # # # #  # # #  # # # #  # # # #  # #  # # # # 
def inputFloatLow(message,lowBound)
    while True:
        result=inputFloat(message)
        if result<lowBound
            print("Please enter a value greater than or equal to ",lowBound)
        else:
            break
    return result
# # # # # # # #  # # # #  # #  # # # #  # # #  # # # #  # # # # # # 
def inputFloatHigh(message,highBound)
    while True:
        result=inputFloat(message)
        if result>highBound
            print("Please enter a value less than or equal to ",highBound)
        else:
            break
    return result
# #  # # #  # # # # # #  # # #  # # #  # # # # #  # # # #  # # #  # 
def inputFloatBetween(message,lowBound,highBound)
    while True:
        result=inputFloat(message)
        if result<lowBound:
            print("Please enter a value greater than ",lowBound)
        elif result>highBound:
            print("Please enter a value less than ",highBound)
        else:
            break
    return result
######################################Integers##################################

def isInteger:
    try:
        int(string)
        return True
    except ValueError:
        return False
        
# # # # # # # #  # # # #  # # # #  # # # #  # # #  # # # # 
def inputInteger(message):
        while True:
            result=input(message)
            if isInteger(result):
                result=int(result)
                break
            else:
                print("please enter a valid integer value!")
        return result
#  # # #  # # # #  # #  # # #  # # #  # # #  # # #   #  # # #
def inputIntegerLow(message,lowBound)
    while True:
        result=inputInteger(message)
        if result<lowBound
            print("Please enter a value greater than ",lowBound)
        else:
            break
    return result
#  # #  # # #  # # #  # # #  # # # # #  # # #  # # # #  # # # #
def inputIntegerHigh(message,highBound)
    while True:
        result=inputInteger(message)
        if result>highBound
            print("Please enter a value less than or equal to ",highBound)
        else:
            break
    return result
# # #  # # # #  # # #  # # #  # # #  # # # # # #  # # # #  # ## 
def inputIntegerBetween(message,lowBound,highBound)
    while True:
        result=inputInteger(message)
        if result<lowBound:
            print("Please enter a value greater than ",lowBound)
        elif result>highBound:
            print("Please enter a value less than ",highBound)
        else:
            break
    return result
##########################other###############################
def obtainYesNo(message):
    while True:
        result = input(message+"(y/n): ")
        result = result.lower()
        if result == "y" or result == "n":
            break; 
    return result




