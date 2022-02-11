x = input("Please Enter First Digit ")
y = input("Please Enter Second Digit ")

# string.isdigit()
if ( x.isdigit() == True and y.isdigit() == True ):
    print ("You entered ", x )
    print ("You entered ", y )
else:
    print ("You did not enter a number")
    exit()

choice = input("Would you like to add enter 0 or multiply enter 1 ?")
if ( choice == "0" ):
    print ( "Results ", int(x) + int(y) )
elif ( choice == "1" ):
    print ( "Results ", int(x) * int(y) )
else:
    print ("You did not enter a 0 or 1")
