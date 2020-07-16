#Author: Erik Blackowicz
#Date: 7/15/20
#Description: Creates multiply fx using recursive addition
# Recursive addition - reduces 'a' by 1 until reaches 0, then returns to base case to add 'b' value 'a' amount of times.

def multiply(a,b):
  ''' takes in two positive integer parameters and multiplies them using recursive addition.'''
  if a == 0 or b == 0: # base case
    return 0
  else: # starts recursive case
    return b + multiply(a-1, b)
