# https://leetcode.com/problems/consecutive-characters
# class Solution:
#     def maxPower(self, s: str) -> int:
# def maxPower(s):
#     # Assign variables
#     ans = 0
#     consec_count_per_letter = 1
#     prev_letter = s[0]

#     # Return 1 when the length of the input is 1
#     if len(s) == 1:
#         return 1

#     # Loop from 1 to the length of the input
#     for i in range(1, len(s)):
#         # If the current letter is the same as the prev letter,
#         # then add 1 to consec_count_per_letter
#         if s[i] == prev_letter:
#             consec_count_per_letter += 1
#         else:
#             consec_count_per_letter = 1

#         # Update the prev letter
#         prev_letter = s[i]
#         # Update the answer with a maximum
#         # between the answer and consec_count_per_letter
#         ans = max(ans, consec_count_per_letter)

#     return ans

def maxPower(s):
    ans = 1
    curr_max = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            curr_max += 1
            ans = max(ans, curr_max)
        else:
            curr_max = 1
    return ans


assert(maxPower("leetcode")) == 2
assert(maxPower("abbcccddddeeeeedcba")) == 5
assert(maxPower("triplepillooooow")) == 5
assert(maxPower("hooraaaaaaaaaaay")) == 11
assert(maxPower("tourist")) == 1