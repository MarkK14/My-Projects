def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

rate=35

hours=input("how many hours did you work? ")
sales=input("how much did you make in sales? ")
validHours=isfloat(hours)and float(hours)>=0
validSales=isfloat(sales) and float(sales)
if not validSales and not validSales:
    print("both sales and hours are invalid")
elif not isfloat(hours):
    print("Invalid hours")
elif not isfloat(sales):
    print("Invalid Sales")
hours=float(hours)
sales=float(sales)
if sales<=5000:
    commission=sales*0.04
elif 5000<sales<=15000:
    commission=200+sales*0.06
elif 15000<sales:
    commission=1100+sales*0.08
pay=hours*rate+commission
pay=str(pay)
print("your pay is $"+pay)
