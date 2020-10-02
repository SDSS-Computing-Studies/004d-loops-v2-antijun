"""
Problem 2:
inputs:
int number

outputs:
"xx! is yy" where xx is the integer entered and yy is the calculated answer

example:
Enter a number: 4
4! is 24
"""

x = int(input("Enter a number: "))
y = 1
strx = str(x)

for i in range(1, x+1):
    y = y*i

stry = str(y)
print(strx + "! is " + stry)
