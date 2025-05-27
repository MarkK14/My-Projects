def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
#Main Program
print ("Welcome to the Greatest Calculator to ever Exist")
length = input ("What is the length of the Rectangular prism? ")
width = input ("What is the width of the rectangular prism? ")
height = input ("What is the height of the rectangular prism? ")
if not isfloat(length):
    print("Totally NOT Tubular DUDE! That Length is invalid")
elif not isfloat(width):
    print("Whoa DUDE, not Cool! the width is invalid bro.")
elif not isfloat(height):
    print("Buddy, wdytya u needa give me a valid height broski")
else:
    length = float (length)
    width = float (width)
    height = float (height)
    volume = length * width * height
    surfaceArea = 2 * ((length * width) + (length + height) + (width * height))
    print (f"Your Rectangular prism has volume:{volume}cm^3")
    print(f"and surface area:{surfaceArea}cm^2")


