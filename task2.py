"""

Task 2:
inputs:
str name

outputs:
"That name is in the list"
"That name is not in the list"

example:
Enter a name: Grace
That name is not on the list

example:
Enter a name: Lebron
That name is on the list

"""

name = input("Enter a name: ")

nameList = ("Lebron","Kobe","Michale","Shaq","Dennis")

for i in nameList:
    if name == i:
        print("That name is on the list")

if name not in nameList:
        print("That name is not on the list")


    
     

