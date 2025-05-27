#############################################################################################################
# the Deduction Payroll Calculator
# Written By: Mark Khairallah
# Filename: PayrollDeduction.py
# Project Started On: Oct 2nd 2023
# Project Finished On: Oct 5th 2023
# Project Prepared for: E. DiAntonio
# Description of Project: 
# This program calculates the user's Take-home pay after taxes and deductions.
#############################################################################################################
# Functions Used
#############################################################################################################
# Function isFloat
# isFloat - Boolean function which accepts with one string parameter. It returns a Boolean result indicating
#           whether the string parameter consists of a valid floating point number. 
# Return Value and Types:
#   Boolean value 
def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
#############################################################################################################
#Main Program
#############################################################################################################
# Variables Used
# annualEarnBD  type:float  User's Annual Earnings before deductions (gross pay)
#cityOfBirth    type:string User's city of birth (used to determine provincial taxes)
#validCity      type:boolean variable based on whether the city of birth is a valid city
#fedTax:        type:float  Federal Tax (how much is payed as federal tax)
#provTax:       type:float  Provincial Tax. Based on user's city of birth (how much is payed as provincial tax)
#pensionP:      type:float  Pension plan contributions.(how much is payed as pension plan contributions)
#emplInsPrem    type:float  Employment Insurance Premium.(how much is payed as employment insurance premium)
#thPay          type:float  Take-Home Pay (earnings after taxes and deductions)
###########################################################################################################
print ("Welcome to the Deduction Payroll Calculator")

#Prompt user for their annual earnings and city of birth
annualEarnBD = input("Enter your annual earnings before deductions: ")
cityOfBirth = input("Enter your city of birth (Sesame Place, Quahog, Springfield, or Minionland): ")

#utilising string methods so that I can check whether or not cityOfBirth is a valid cityOfBirth
cityOfBirth = cityOfBirth.lower().strip() 

#valid city is either True or False depending on whether cityOfBirth is a valid city
validCity = cityOfBirth == "sesame place" or cityOfBirth == "quahog" or cityOfBirth == "springfield" or cityOfBirth == "minionland"

#Ensures that if annualEarnBD is a float or the cityOfBirth is not a valid city display error message
if not isfloat(annualEarnBD) or not validCity:
    if not isfloat(annualEarnBD):
        print ("You have entered an invalid annual salary. Please re-run the program and try again.")
    elif not validCity:
        print ("You have specified a city which is not known to us. Please re-run the program and try again.")
else:
    #convert user entered values into float values
    annualEarnBD = float(annualEarnBD)
    
    #calculates federal tax based on gross pay
    if 0<annualEarnBD<=20000:
        fedTax = annualEarnBD*0.12
    elif 20000<annualEarnBD<=120000:
        fedTax = 2400+(annualEarnBD-20000)*0.18
    elif 120000<annualEarnBD:
        fedTax = 24000+(annualEarnBD-120000)*0.25
    
    #calculates provincial tax based on city of birth and then gross pay
    if cityOfBirth == "sesame place":
        if annualEarnBD<=100000:
            provTax = 0.00
        elif 100000<annualEarnBD:
            provTax = (annualEarnBD-100000)*0.08
    elif cityOfBirth == "quahog":
        if annualEarnBD<=75000:
            provTax = annualEarnBD*0.05
        elif 75000<annualEarnBD:
            provTax=3750+(annualEarnBD-75000)*0.08
    elif cityOfBirth == "springfield":
        provTax = 0.000
    elif cityOfBirth == "minionland":
        provTax = (annualEarnBD)*0.02
        
    #calculates pension plan contributions
    pensionP = annualEarnBD*0.045
    
    #sets a maximum deduction on pension plan contributions
    if pensionP>2925:
        pensionP = "2925.00"
    
    #calculates employment insurance premium
    emplInsPrem = annualEarnBD*0.0155
    
    #sets a maximum deduction on employment insurance premium
    if emplInsPrem>800:
        emplInsPrem = "800.00"
    
    #calculates Take Home Pay
    thPay = annualEarnBD-fedTax-provTax-pensionP-emplInsPrem
    
    #rounds all variable
    annualEarnBD = round(annualEarnBD,2)
    fedTax = round(fedTax,2)
    provTax = round(provTax,2)
    pensionP = round(pensionP,2)
    emplInsPrem = round(emplInsPrem,2)
    thPay = round(thPay,2)
    
    #Display result of calculation
    print ("===== Payroll Calculation Results =====")
    print (f"Annual Earnings (Before Deductions): ${annualEarnBD}")
    print (f"Federal Taxes: ${fedTax}")
    print (f"Provincial Taxes: ${provTax}")
    print (f"Pension Plan Contributions: ${pensionP}")
    print (f"Employment Insurance Premium: ${emplInsPrem}")
    print (f"Take-Home Pay: ${thPay}")
# Display comedic program termination messages :)
print ("\n\nThank you for using the Paycheck Deduction Program")
print ("Be sure to send $2.99 to:")
print ("\t\tMarksoft Inc.")
print ("\t\tc/o Mark Khairallah")
print ("\t\t2800 Erin Centre Boulevard ")
print ("\t\tMississauga,ON")
    


