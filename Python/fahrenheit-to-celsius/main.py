def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
#Main Program

print("Welcome to Thermonator")
choice= input("Would you like to convert from Celsius to Fahrenheit or Fahrenheit to Celsius? ")
choice= choice.lower().strip()
if choice=="fahrenheit to celsius":
    tempF = input ("What is the current temperature in fahrenheit? ")
    if not isfloat(temF):
        print("Please enter a valid temperature")
    else:
            tempC = (5 / 9 * (int (tempF) - 32))
        if tempC>=40:
            print("OUCH Thats HOT!")
        elif tempC<=0:
            print("Ooh Thats a bit chilly Eh?")
        print (f"your current temperature of {tempF}"+
           f" degrees fahrenheit in degrees Celsius is {tempC} degrees")
elif choice=="celsius to fahrenheit":
    tempC= input("What is the temperature in celsius? ")
    if not isfloat(tempC) **************************************************************
    tempF=(int(tempC)*(9/5))+32
    if tempF>=104:
        print("OUCH Thats HOT!")
    elif tempF<=32:
        print("Ooh Thats a bit chilly Eh?")
    print (f"your current temperature of {tempC}"+
       f" degrees celsius in degrees fahrenheit is {tempF} degrees")
else:
    print('Your response of "'+choice+'" is an Invalid response, please choose one of the two options')




