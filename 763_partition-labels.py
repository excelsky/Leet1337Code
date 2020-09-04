# https://leetcode.com/problems/partition-labels
# class Solution:
#     def partitionLabels(self, S: str) -> List[int]:
def partitionLabels(S):
    last_index_d = {letter: index for index, letter in enumerate(S)}
    j = anchor = 0
    ans = []
    for index, letter in enumerate(S):
        j = max(j, last_index_d[letter])
        if index == j:
            ans.append(index + 1 - anchor)
            anchor = index + 1
    return ans

assert(partitionLabels("ababcbacadefegdehijhklij")) == [9, 7, 8]
assert(partitionLabels("abaccbdeffed")) == [6, 6]