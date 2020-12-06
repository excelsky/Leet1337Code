# https://leetcode.com/problems/valid-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        open_par = ["(", "{", "["]
        close_par = [")", "}", "]"]
        ans = []
        for ss in s:
            if ss in open_par:
                ans.append(ss)
            if ss in close_par:
                if ans == []:
                    return False
                if open_par.index(ans[-1]) == close_par.index(ss):
                    ans.pop()
                else:
                    return False
        return ans == []
