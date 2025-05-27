def isfloat:
    try:
        float(string)
        return True
    except ValueError:
        return False

def inputFloat(message):
        while True:
            result=input(message)
            if isFloat(result):
                result=float(result)
                break
            else:
                print("please enter a valid float value!")
        return result


def isInteger:
    try:
        int(string)
        return True
    except ValueError:
        return False
        

def inputInteger(message):
        while True:
            result=input(message)
            if isInteger(result):
                result=int(result)
                break
            else:
                print("please enter a valid integer value!")
        return result

