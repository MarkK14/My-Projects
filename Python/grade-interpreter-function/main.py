def getResult(mark):
    if mark<0:
        message="It is impossible to get a negative mark"
    elif 50>mark>=0:
        message="You must attend summer school"
    elif 100>=mark>80:
        message="u got an A!"
    elif 80>=mark>70:
        message="u got a B!"
    elif 70>=mark>60:
        message="u got a C!"
    elif 60>=mark>=50:
        message="u got a D!"
    else:
        message="your mark is too high"
    return message

grade=input("Insert grade: ")
grade=int(grade)

print(getResult(grade))
