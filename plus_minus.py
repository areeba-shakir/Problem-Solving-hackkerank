# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the decimal.

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    d = {}
    for i in range(len(arr)):
        if arr[i] > 0:
            d.update({'p': d.get('p', 0) + 1})
        elif arr[i] < 0:
            d.update({'n': d.get('n', 0) + 1})
        else:
            d.update({'0': d.get('0', 0) + 1})

    print("{:.6f}".format(d['p'] / len(arr)))
    print("{:.6f}".format(d['n'] / len(arr)))
    print("{:.6f}".format(d['0'] / len(arr)))
