#Author:Erik Blackowicz
#Date: 7/15/20
#Description: Project 5a. Creates multiply fx (product of 2 integers) by using recursive addition.
# Does not work if both integers are negative. Recursive addition action - reduces 'num1' condition by 1 until reaches 0,
# then returns to the base case to add 'num2' value 'num1' amount of times.

def multiply(num1,num2): # num2 can be a negative value, num1 must be positive value
  ''' Takes in two positive integer parameters and multiplies them using recursive addition. Num2 can be a negative value'''
  if num1 == 0 or num2 == 0: # base case
    return 0
  else: # starts recursive case
    return num2 + multiply(num1-1, num2)
