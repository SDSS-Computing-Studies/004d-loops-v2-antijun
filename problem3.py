"""
Problem 3:
input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

x = int(input("Enter an integer less than 10: "))
y = 0
for i in range(1, x+1):
    y = y+1
    stry = str(y)
    print(stry, end="")
