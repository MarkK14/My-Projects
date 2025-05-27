#Khairallah Restaurant
#The following Program will allow customers to order Shawerma and only Shawerma
#it will then Calculate the price and the number of boxes, bags and individually wrapped shawermas
#It will ask for a tip
#the total cost is calculated based on the following pricing scheme:

tax = 1.13
boxSize = 10
bagSize = 3
boxCost = 13.49
bagCost = 7.49
singleCost = 1.99
 
print ("Khairallah Restaurant corp. (c)KhairallahInc.")
nameFood = input ("\n\nwelcome to Mark's Shawerma Shack. What you would like? ")
shawerma = input (f"Sorry we don't have {nameFood}, we only have Shawerma ... would you like Shawerma? YES?! ok how many? ")
shawerma = int (shawerma)
boxes = shawerma	//boxSize
leftOver = shawerma % boxSize
bags = leftOver     //bagSize
totalLeftOver = leftOver %bagSize
totalCost = ((boxes * boxCost) + (bags * bagCost) + (totalLeftOver * singleCost)) * tax
totalCost = round (totalCost , 2)
print (f"Your total today is ... ${totalCost}")
shawermaAvg = totalCost /shawerma
shawermaAvg = round (shawermaAvg , 2)
print (f"Shawerma Fun Fact: Today you're paying Approximately ${shawermaAvg} per Shawerma. Nice!")
print (f"Here is/are your " + str(boxes) + " box(es) and " + str(bags) + " bag(s) of Shawerma")
print (f"There is/are " + str(totalLeftOver) + " shawerma(s) wrapped seperately")
tip = input ("Would you like to leave tip? How much? ")
tip=float(tip)
if tip<20:
    newTip = input (f"Only {tip}% ?!?! C'mon give me some more... ")
    newTip = float (newTip)
    tipTotal = totalCost * (newTip * 0.01)
    tipTotal = round(tipTotal , 2)
    bigNumber = (totalCost * shawerma) **boxCost
    print (f"Ok Thank you for your ${tipTotal} tip")
else:
    tipNum=totalCost*(tip*0.01)
    tipNum=round(tipNum,2)
    print (f"Ok Thank you for your ${tipNum} tip")
print ("\n\nThats a wrap for today folks. Thank You for using this online Cashier. Have a shawerma-ful day!")
print (f"\t\tYou owe ${bigNumber} to:")
print ("\t\tKhairallah Inc.")
print ("\t\t100 Road to Nowhere")
print ("\t\tPunkeydoodles Corners, Ontario")
