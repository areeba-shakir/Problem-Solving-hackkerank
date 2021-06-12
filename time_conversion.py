# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
#
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    if 'AM' in s:
        if s[:2] == '12':
            return '00'+s[2:8]
        else:
            return s[:8]
    else:
        if s[:2] == '12':
            return s[:8]
        else:
            return str(int(s[:2])+12) + s[2:8]