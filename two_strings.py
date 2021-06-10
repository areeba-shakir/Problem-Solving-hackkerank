# Given two strings, determine if they share a common substring.
# A substring may be as small as one character.
#
# Example
# s1 = 'and'
# s2 = 'art'
# These share the common substring a.
#


def twoStrings(s1, s2):
    # Write your code here
    if set(s1) & set(s2):
        return 'YES'
    else:
        return 'NO'

