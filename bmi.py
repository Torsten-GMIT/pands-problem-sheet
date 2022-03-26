# Task week 02
# Author: Torsten Kindt

# Writing a small program to calculate Body Mass Index (BMI)
# Formula for BMI taken from task, then tried until a working solution was found 

weight = int(input("Enter your weight in kg here:"))
height = int(input("Enter your height in cm here:"))

heightsq = (height/100) * (height/100)

answer = weight / heightsq

print("Your BMI is: " + str(round(answer, 2)))

