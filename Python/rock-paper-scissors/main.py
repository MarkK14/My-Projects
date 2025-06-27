from InpExt import *
import random
random.seed()

def userPick():
    while True:
        choice=input("Rock Paper Scissors Lizard Spock! what did you choose? ")
        choice=choice.title().strip()
        if choice=="Rock" or choice=="Paper" or choice=="Scissors" or choice=="Lizard" or choice=="Spock":
            break
        else:
            print("Choose either Rock Paper Scissors Lizard or Spock")
    return choice
def comPick():
    comChoice=random.randint(1,5)
    if comChoice == 1:
        return"Rock"
    elif comChoice ==2:
        return"Paper"
    elif comChoice ==3:
        return "Scissors"
    elif comChoice ==4:
        return"Lizard"
    else:
        return "Spock"
def winner (userChoice,comChoice):
    if userChoice == comChoice:
        return "Tie"
        
    elif ((userChoice=="Rock" and (comChoice =="Scissors" or comChoice=="Lizard")) or 
            (userChoice=="Paper" and (comChoice =="Rock" or comChoice=="Spock")) or 
            (userChoice=="Scissors" and (comChoice =="Paper" or comChoice=="Lizard"))or
            (userChoice=="Lizard" and (comChoice=="Paper" or comChoice=="Spock")) or
            userChoice=="Spock" and (comChoice=="Rock" or comChoice=="Scissors")):
        return "Player"
    else:
        return "Computer"


################################################################################
oneMore=True
while oneMore:
    playAgain=True
    userScore=0
    comScore=0
    print("Welcome to Rock Paper Scissors Lizard Spock ... LET'S PLAY")
    userName=input("Enter Name: ")
    while playAgain:
        comChoice=comPick()
        userChoice=userPick()
        verdict=winner(userChoice,comChoice)
        
        if verdict == "Player":
            userScore +=1 
            print(f"Aw Man I chose {comChoice} ... You WIN!")
        elif verdict == "Computer":
            comScore+=1
            print(f"Ha Ha I chose {comChoice} ... You LOSE!")
        print("The current score is "+userName+f" {userScore}-{comScore} Computer")
    oneMore=obtainYesNo("One more round?") == 'y'
    if not oneMore: 
        break
    
print("Good-bye")
print("\n\n The Final score is...")
print("\t\t"+userName+f" {userScore}-{comScore} Computer")
    
    