# https://leetcode.com/problems/goat-latin
# class Solution:
#     def toGoatLatin(self, S: str) -> str:
def toGoatLatin(S):
    vowels = "aeiouAEIOU"
    s = S.split()
    for i in range(len(s)):
        if s[i][0] not in vowels:
            s[i] = s[i][1:] + s[i][0]
        s[i] += "ma" + (i+1) * "a"
    return " ".join(s)

# toGoatLatin("I speak Goat Latin")
assert(toGoatLatin("I speak Goat Latin")) == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
assert(toGoatLatin("The quick brown fox jumped over the lazy dog")) == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"