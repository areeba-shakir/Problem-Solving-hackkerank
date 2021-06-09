# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like
# topography. During his last hike, he took exactly n steps. For every step he took, he noted if it was an uphill
# or a downhill step. Gary's hikes start and end at sea level. We define the following terms:
# A mountain is a non-empty sequence of consecutive steps above sea level, starting with a step up from
# sea level and ending with a step down to sea level.
# A valley is a non-empty sequence of consecutive steps below sea level, starting with a step down from
# sea level and ending with a step up to sea level.
# Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he
# walked through.

# ---------- Counting Valleys ----------
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    valleys = 0
    for p in range(len(path)):
        if sea_level == 0 and path[p] == 'D':
            valleys = valleys + 1

        if path[p] == 'D':
            sea_level = sea_level - 1
        else:
            sea_level = sea_level + 1
    return valleys




