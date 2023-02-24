#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2
import math
varA = input("we are going to solve the algebra equation: ax + b = c \nplease input a: ")
varB = input("please input b: ")
varC = input("please input c: ")

varA = int(varA)
varB = int(varB)
varC = int(varC)

x = (varC - varB) / varA

print(f"x = {x}")