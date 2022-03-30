 # Task week 03
 # Author: Torsten Kindt

 # A program that asks a user to input a string and outputs every second letter in reverse order.


string = input("Enter a string: ")
outString = (string[::-1])

print("Your string is '{}'. Every second letter in reverse order of that string is '{}'.".format(string, outString[::2]))

# answer inspired by https://stackoverflow.com/questions/663171/how-do-i-get-a-substring-of-a-string-in-python 
# and https://www.w3schools.com/python/python_howto_reverse_string.asp
