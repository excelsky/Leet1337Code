# https://leetcode.com/problems/thousand-separator
# class Solution:
#     def thousandSeparator(self, n: int) -> str:
def thousandSeparator(n):
    # Assign variables
    s = str(n)
    reversed_s = s[::-1]
    length = len(reversed_s)

    # Check the case when a thousand seperator is not needed
    if length <= 3:
        return s

    # Assign answer variable from the reversed string
    ans = reversed_s[0]
    # Loop through [1, length of the string)
    for i in range(1, length):
        ans += reversed_s[i]
        # Add a thousand seperator
        if i % 3 == 2 and i + 1 != length:
            ans += "."

    # Return as regular (aka non-reverse)
    return ans[::-1]
    

assert(thousandSeparator(987)) == "987"
assert(thousandSeparator(1234)) == "1.234"
assert(thousandSeparator(123456789)) == "123.456.789"
assert(thousandSeparator(0)) == "0"