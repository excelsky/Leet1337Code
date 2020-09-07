# https://leetcode.com/problems/word-pattern
# class Solution:
#     def wordPattern(self, pattern: str, str: str) -> bool:
def wordPattern(pattern, str):
    # str_l = str.split(" ")    
    # if len(pattern) != len(str_l):
    #     return False
    # d = dict()
    # for i in range(len(pattern)):
    #     if i == 0:
    #         d[pattern[i]] = str_l[i]
    #     else:
    #         if pattern[i] in d.keys():
    #             if d[pattern[i]] != str_l[i]:
    #                 return False
    #         else:
    #             d[pattern[i]] = str_l[i]
    # if len(d.values()) > len(set(d.values())):
    #     return False
    # return True
    pattern_l, str_l = list(pattern), str.split()
    return list(map(pattern_l.index, pattern_l)) == list(map(str_l.index, str_l))


assert(wordPattern(pattern = "abba", str = "dog cat cat dog")) == True
assert(wordPattern(pattern = "abba", str = "dog cat cat fish")) == False
assert(wordPattern(pattern = "aaaa", str = "dog cat cat dog")) == False
assert(wordPattern(pattern = "abba", str = "dog dog dog dog")) == False