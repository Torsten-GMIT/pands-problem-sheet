# Task week 04
# Author: Torsten Kindt

# A program that asks a user to input a positive Integer and outputs the successive values of the Collatz Conjecture, otherwise known as the 3x+1 problem: At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.

# solution inspired by https://www.webucator.com/article/collatz-conjecture-in-python/  and  https://www.pythonpool.com/collatz-sequence-python/ 



num = int(input("Enter a positive integer:"))

while (num != 1):
    print(int(num), end =', ')
    if (num % 2) == 0:
        num = (num / 2)
    else:
        num = ((num*3) + 1)
print(int(num))

