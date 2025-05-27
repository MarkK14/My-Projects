hours=input("How many hours did you work? ")
hours=hours.strip()
hours=int(hours)
if 0<hours<=40:
    normPay=hours*15
    normPay=str(normPay)
    print("your pay is $"+normPay )
elif hours>40:
    xtraHoursPay=(1.5*(hours-40)*15)+600
    xtraHoursPay=str(xtraHoursPay)
    print("your pay is $"+xtraHoursPay)
else:
    print("Invalid number of hours entered")
print("Good-Bye")
