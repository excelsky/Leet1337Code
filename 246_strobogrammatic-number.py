# https://leetcode.com/problems/strobogrammatic-number

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        stro_d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        for i in range(len(num) //2 + 1):
            forward = num[i]
            if forward in stro_d.keys():
                value = stro_d[forward]
            else:
                return False
            backward = num[-i-1]
            if value != backward:
                return False
        return True
        