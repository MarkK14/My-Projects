from InpExt import *
import random
random.seed

print ("Welcome tooooooo ... Guess that Number!")
secretNumber=random.randint(1,100)
guessCount=0

correctGuess = False
tryAgain = True
playAgain=True
while playAgain:
    while not correctGuess and tryAgain and guessCount<5:
        guess=inputIntegerBetween("Make your Guess. What do you think the number is? ",1,100)
        guessCount +=1
        if guess>secretNumber:
            print("too High")
        elif guess<secretNumber:
            print("too Low")
        else:
            print("YOU GOT IT! WOW")
            correctGuess=True
        if not correctGuess and guessCount<5:
            tryAgain=obtainYesNo("try Again? ")
            if tryAgain=="n":
                break
    if guessCount==5 or correctGuess:
        print("GAME OVER")
        playAgain=obtainYesNo("\t\tDo you wanna Play Again? ")
        if playAgain=="y":
            playAgain=True
            guessCount=0
            correctGuess=False
        elif playAgain=="n":
            break
print("Good-Bye")

