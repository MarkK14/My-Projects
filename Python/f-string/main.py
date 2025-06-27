userName="Kladdy"
age=28
favouriteNumber=111333
hairLost=favouriteNumber*age
print("0123456789"*8)
print(f"Right justify within 20 characters: {userName:>20}. Cool eh?")
print(f"Left justify within 20 characters: {userName:<20}. Cool eh?")
print(f"Center within 20 characters: {userName:^20}. Cool eh?")
print(f"Accidental typo I found: {userName:*^20}. Nice?")
print(f"Favourite number is:{favouriteNumber:.2f}.WOW!")
print(f"Favourite Number is:{favouriteNumber:8.2f}.WOW!")
print(f"Favourite Number is:{favouriteNumber:8.4f}.WOW!")
print(f"A lot of hair is {favouriteNumber:.2f} is {hairLost:<12.2f}.wdtya")
print(f"A lot of hair is {favouriteNumber:.2f} is {hairLost:^12.2f}.wdytya")
print(f"A lot of hair is {favouriteNumber:.2f} is {hairLost:>12.2f}.wdytya")