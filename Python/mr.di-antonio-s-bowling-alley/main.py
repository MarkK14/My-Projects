
from InpExt import *

def bowlerRating(score):
    if score == 300:
        return "100% LEGENDA AMAZINGO PARAFISSIMO"
    elif score>275:
        return"GOAT"
    elif score>225:
        return"Legend"
    elif score>175:
        return"World Class"
    elif score >125:
        return"Decent"
    elif score>0:
        return"Wow ... you are BAD"
    else:
        return"thats not even a score"
        
def diGreeting(day,students):
    day=day.title()
    
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday":
        result= "Bye, have a nice Weekend!"
    elif day=="Friday":
        result= "see you tomorrow"
    elif day=="Saturday" or day=="Sunday":
        return"It's the weekend get outta here!"
    else:
        result="thats not a day"
    if students>10:
        result+=" I won't miss you"
    else:
        result+=" fine I will miss you"
    return result


runAgain=True
while runAgain:
    day=input("What Day is it Today? ")
    students=inputIntegerLow("How many students are in the class now? ",0)
    score=inputIntegerBetween("What is your score? ",0,300)
    print(bowlerRating(score))
    
    again=obtainYesNo("Do you need another Rating?")
    if again=="n":
        runAgain=False

print(diGreeting(day,students))