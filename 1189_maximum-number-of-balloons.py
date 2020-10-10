# https://leetcode.com/problems/maximum-number-of-balloons
# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         balloon_s = "balloon"
#         balloon_l = list(balloon_s)
#         ans = 0
#         for t in text:
#             if t in balloon_s:
#                 print(t, balloon_l)
#                 balloon_l.remove(t)
#             if balloon_l == []:
#                 ans += 1
#                 balloon_l = list(balloon_s)
#         return ans
def maxNumberOfBalloons(text):
    return min(text.count("b"), text.count("a"), text.count("l") // 2, text.count("o") // 2, text.count("n"))
        


assert(maxNumberOfBalloons("nlaebolko")) == 1
assert(maxNumberOfBalloons("loonbalxballpoon")) == 2
assert(maxNumberOfBalloons("leetcode")) == 0
t = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
assert(maxNumberOfBalloons(t)) == 10