age=input("How old are you? ")
age=int(age)
if age<18:
    time=18-age
    print(f"Sorry you're too young to vote see you in {time} years")
else:
    print("you are elegible to vote ... Nice!")