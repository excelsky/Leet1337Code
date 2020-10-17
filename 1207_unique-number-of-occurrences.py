# https://leetcode.com/problems/unique-number-of-occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Assign a dictionary
        d = dict()

        # Loop through the input array
        for a in arr:
            # If the element is in the dictionary,
            # then we increment its count by 1
            if a in d.keys():
                d[a] += 1
            # If the element is not in the dictionary,
            # then we initialize its count by 1
            else:
                d[a] = 1

        # Assign a value list from the dictionary values
        val_l = sorted(list(d.values()))

        # Loop through the range of the value list from 1
        for i in range(1, len(val_l)):
            # If the current and the previous values are the same,
            # then we return False
            if val_l[i] == val_l[i-1]:
                return False

        # If everything above passes, then we return True.
        return True
