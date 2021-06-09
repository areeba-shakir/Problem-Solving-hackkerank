# Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale.
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# For example, there are n = 7 socks with colors ar = [1,2,1,2,1,3,2]. There is one pair of color 1 and one of color 2
# There are three odd socks left, one of each color. The number of pairs is 2.
# Function Description
# Complete the sockMerchant function in the editor below. It must return an integer representing the number of
# matching pairs of socks that are available.
# sockMerchant has the following parameter(s):
# n: the number of socks in the pile
# ar: the colors of each sock
# Input Format
# The first line contains an integer n, the number of socks represented in ar.
# The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.
# Output Format
# Return the total number of matching pairs of socks that Alex can sell.


#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


# ---------- SOLUTION USING Counter function ----------
import math
import os
import random
import re
import sys
from collections import Counter

def sockMerchant(n, ar):
    # Write your code here
    count = Counter(ar)
    values = count.values()
    return sum(i // 2 for i in values)



# ---------- SOLUTION USING sorting ----------
import math
import os
import random
import re
import sys
from collections import Counter

def sockMerchant(n, ar):
    # Write your code here
    sorted_array = sorted(ar)
    pairs = 0
    i = 0
    while i < n - 1:
        if sorted_array[i] == sorted_array[i + 1]:
            pairs = pairs + 1
            i = i + 2
        else:
            i = i + 1
    return pairs
