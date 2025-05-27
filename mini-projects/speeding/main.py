def calcDemP(overLimit):
    if 0<overLimit<16:
        demeritPoints=0
    elif 16<=overLimit<=29:
        demeritPoints=3
    elif 30<=overLimit<=49:
        demeritPoints=4
    else:
        demeritPoints=6
    return demeritPoints
def isInteger(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def dollarFine(overLimit):
    if 0<overLimit<20:
        fine=overLimit*3
    elif overLimit<30:
        fine=overLimit*4.5
    elif overLimit<50:
        fine=overLimit*7
    else:
        fine=overLimit*9.75
    return fine

##############################################################################################################################
######################################################## MAIN PROGRAM ########################################################
##############################################################################################################################
speedLimit=inputIntegerLow("What was the posted Speed limt in km/h? ",0)
speeding=inputIntegerLow("And how fast were you going...? ",0)

overLimit=int(speeding)-int(speedLimit)
runAgain=True:
    
    if overLimit>0:
        demeritPoints=calcDemP(overLimit)
        amountOwing=dollarFine(overLimit)
        print(f"you will receive {demeritPoints}demeritPoints and a fine of ${amountOwing}")
        int(speeding)<0 and int(speedLimit)<0:
            print("Both your inputs are negative. Please re-reun and try again.")
        elif int(speeding)<0:
            print("your speed cannot be negative")
        elif int(speedLimit)<0:
            print("the speed limit cannot be negative")
        elif int(speeding) and int(speedLimit):
            if overLimit<16:
                print("You are not speeding!")



