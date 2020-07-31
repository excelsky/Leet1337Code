## https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

# def solution(s): 
#     current_len = 1
#     max_len = 1
#     prev_i = 0
  
#     alphabet_list = [-1] * 256
#     alphabet_list[ord(s[0])] = 0
  
#     for current_i in range(1, len(s)): 
#         prev_i = alphabet_list[ord(s[current_i])] 
  
#         if prev_i == -1:
#             current_len += 1

#         elif current_len < current_i - prev_i:
#             current_len += 1
  
#         else: 
#             if current_len > max_len: 
#                 max_len = current_len 
#             current_len = current_i - prev_i 
  
#         alphabet_list[ord(s[current_i])] = current_i

#     if current_len > max_len: 
#         max_len = current_len 
  
#     return max_len


def solution(s):
    ans = {}
    ans[0] = s[0]
    for i in range(1, len(s)):
        # if len(ans) >= 2:
        #     key_list = sorted([i for i in ans.keys()])
        #     if key_list[-1] - key_list[-2]
        if i-1 in ans.keys() and s[i] != ans[i-1] and s[i] not in ans.values():
            ans[i] = s[i]
        elif i-1 in ans.keys() and s[i] == ans[i-1]:
            del ans[i-1]
            ans[i] = s[i]
    print(ans)
    return len(ans)


s = "nndfddf"
assert solution(s) == 3
print("1/2")

s = "nndddnf"
assert solution(s) == 3
print("2/2")