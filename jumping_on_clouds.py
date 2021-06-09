# There is a new mobile game that starts with consecutively numbered clouds.
# Some of the clouds are thunderheads and others are cumulus.
# The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
# The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting
# postion to the last cloud. It is always possible to win the game.
#
# For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.

def jumpingOnClouds(c):
    n = len(c)
    index, count = 0, 0
    while index < n - 1:
        if index + 2 < n:
            if c[index + 2] == 1:
                index = index + 1
            else:
                index = index + 2
        elif c[index + 1] == 0:
            index = index + 1
        else:
            break
        count = count + 1

    return count