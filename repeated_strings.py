# There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer n , find and print the number of letter a's in the first n letters of the infinite string.
#
# Example
# s = 'abcac'
# n = 10
# The substring we consider is abcacabcac, the first  characters of the infinite string. There are 4 occurrences of a in the substring.
#
# Function Description
#
# Complete the repeatedString function in the editor below.
#
# repeatedString has the following parameter(s):
#
# s: a string to repeat
# n: the number of characters to consider
# Returns
#
# int: the frequency of a in the substring

# ---------- Using for loops ----------

def repeatedString(s, n):
    # Write your code here
    _s = ''
    count = 0
    for i in range(n):
        for j in s:
            if len(_s) == n:
                break
            _s = _s + j
    for k in _s:
        if k == 'a':
            count = count + 1

    return count


# ---------- Without loop ----------
def repeatedString(s, n):
    # Write your code here
    repeatations = n // len(s)
    if n % len(s) == 0:
        _s = s * repeatations
    else:
        _s = s * repeatations
        remaining = n - len(_s)
        _s = _s + s[:remaining]
    return _s.count('a')


# ---------- Most efficient ----------
def repeatedString(s, n):
    # Write your code here
    repeatations = n // len(s)
    return s.count("a") * repeatations + s[:n - (len(s) * repeatations)].count("a")