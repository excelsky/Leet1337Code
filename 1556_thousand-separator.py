# https://leetcode.com/problems/thousand-separator
# class Solution:
#     def thousandSeparator(self, n: int) -> str:
def thousandSeparator(n):
    # Convert to string
    s = str(n)
    # Edge case
    if len(s) <= 3:
        return s
    increment = -3
    ans = s[increment:]
    # print(ans)
    prev = len(s)
    for i in range(increment, -len(s)-increment, increment):
        print("\ni: ", i)
        left_of_dot = s[i:prev]
        print("left_of_dot: ", left_of_dot)
        print("ans: ", ans)
        ans = left_of_dot + "." + ans
        if prev == len(s):
            prev = increment
        else:
            prev -= i
    return ans



print(thousandSeparator(1234))
# print(thousandSeparator(123456789))