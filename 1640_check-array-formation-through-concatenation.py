# https://leetcode.com/problems/check-array-formation-through-concatenation

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        mapping = {sub_piece[0]: sub_piece for sub_piece in pieces}

        i = 0
        while i < n:
            # find key
            if arr[i] not in mapping.keys():
                return False

            # check value
            sub_piece = mapping[arr[i]]
            for x in sub_piece:
                if x != arr[i]:
                    return False
                i += 1

        return True
