"""
Task 3:
inputs:
none

outputs:
list of numbers
25
10
30
75
20
"""

numList = (25, 8, 10, 11, 33, 30, 51, 75, 63, 14, 20, 99)

for i in numList:
    if i % 5 == 0:
        print(i)