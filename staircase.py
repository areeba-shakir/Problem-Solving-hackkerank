# Staircase detail
#
# This is a staircase of size :
#
#    #
#   ##
#  ###
# ####
# Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.
#
# Write a program that prints a staircase of size n.

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(n):
        print(' '*(n-(i+1)) + '#'*(i+1))
