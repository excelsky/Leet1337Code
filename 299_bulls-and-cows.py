# https://leetcode.com/problems/bulls-and-cows
import collections
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
def getHint(secret, guess):
    # Indices where BULL can be counted
    bull_indices = []
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bull_indices.append(i)

    # Convert to list
    secret_l = list(secret)
    guess_l = list(guess)

    # Pop BULL indices
    if len(bull_indices) == 1:
        secret_l.pop(bull_indices[0])
        guess_l.pop(bull_indices[0])
    else:
        for i in bull_indices[::-1]:
            secret_l.pop(i)
            guess_l.pop(i)

    # Counter dict
    secret_d = collections.Counter(secret_l)
    guess_d = collections.Counter(guess_l)

    # Count COW
    cow_cnt = 0
    for n in secret_d.keys():
        if n in guess_d.keys():
            cow_cnt += min(secret_d[n], guess_d[n])

    # Return
    return "{}A{}B".format(len(bull_indices), cow_cnt)


assert(getHint(secret = "1807", guess = "7810")) == "1A3B"
assert(getHint(secret = "1123", guess = "0111")) == "1A1B"
assert(getHint(secret = "11", guess = "11")) == "2A0B"