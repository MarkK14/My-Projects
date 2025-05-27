initialAmount = input("Initial investment amount: ")
initialAmount = float(initialAmount)

rate = input("Interest Rate (as decimal): ")
rate = float(rate)

periods = input("Number of compounding periods per year: ")
periods = int(periods)

years = input("Enter the number of years for the investment: ")
years = float(years)

if periods == 0:
    print(f"An investment of ${initialAmount:.2f} invested at {rate*100:.2f}%, "
      f"compounded {periods} times per year will grow to $0")
else:
    amount = initialAmount * (1 + rate / periods) ** (periods * years)
    print(f"An investment of ${initialAmount:.2f} invested at {rate*100:.2f}%, "
      f"compounded {periods} times per year will grow to ${amount:.2f}")


