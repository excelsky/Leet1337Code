# https://leetcode.com/problems/compare-version-numbers
# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
def compareVersion(version1, version2):
    version1_l, version2_l = version1.split('.'), version2.split('.')
    l_1, l_2 = len(version1_l), len(version2_l)

    # Loop through the longer list
    for i in range(max(l_1, l_2)):
        # Assign the integer of the element
        # if a position number is smaller than the length of the list
        # else assign 0
        e_1 = int(version1_l[i]) if i < l_1 else 0
        e_2 = int(version2_l[i]) if i < l_2 else 0
        # Compare
        if e_1 > e_2:
            return 1
        if e_1 < e_2:
            return -1

    return 0



assert(compareVersion(version1 = "0.1", version2 = "1.1")) == -1
assert(compareVersion(version1 = "1.0.1", version2 = "1")) == 1
assert(compareVersion(version1 = "7.5.2.4", version2 = "7.5.3")) == -1
assert(compareVersion(version1 = "1.01", version2 = "1.001")) == 0
assert(compareVersion(version1 = "1.0", version2 = "1")) == 0
assert(compareVersion(version1 = "1", version2 = "1.1")) == -1