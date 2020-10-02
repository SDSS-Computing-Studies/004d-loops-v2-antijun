"""
Problem1:
inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****
"""

number = int(input("Enter a number: "))
star = str("*")

for i in range(number):
    print(star*number)
