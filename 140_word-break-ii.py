# https://leetcode.com/problems/word-break-ii/
import collections
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> Set[str]:
def wordBreak(s, wordDict):
    # quick check on the characters,
    #   otherwise it would exceed the time limit for certain test cases.
    if set(collections.Counter(s).keys()) > set(collections.Counter("".join(wordDict)).keys()):
        return []

    wordSet = set(wordDict)

    dp = [[]] * (len(s)+1)
    dp[0] = [""]

    for endIndex in range(1, len(s)+1):
        sublist = []
        # fill up the values in the dp array.
        for startIndex in range(0, endIndex):
            word = s[startIndex:endIndex]
            if word in wordSet:
                for subsentence in dp[startIndex]:
                    sublist.append((subsentence + ' ' + word).strip())

        dp[endIndex] = sublist
    
    return set(dp[len(s)])

assert(wordBreak(s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"])) == {'cat sand dog', 'cats and dog'}
assert(wordBreak(s = "pineapplepenapple", wordDict = ["apple", "pen", "applepen", "pine", "pineapple"])) == {"pine apple pen apple", "pineapple pen apple", "pine applepen apple"}
assert(wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"])) == set()