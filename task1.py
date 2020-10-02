"""
Task 1:
inputs:
int number

outputs:
multiples of that number

example:
Enter number:4
4 8 12 16 20 24 28 32 36 40 44 48

"""


a = int(input("Enter an integer: "))


for i in range(1, 13):
    print(a * i, end=" ")
