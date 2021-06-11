# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#
# For example, the square matrix arr is shown below:
#
# 1 2 3
# 4 5 6
# 9 8 9

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    d1, d2 = 0,0
    index = 0
    for i in arr:
        d1 = d1 + i[index]
        d2 = d2 + i[len(i)-1-index]
        index = index + 1
    return abs(d1-d2)


