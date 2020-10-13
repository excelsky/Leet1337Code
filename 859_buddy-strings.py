# https://leetcode.com/problems/buddy-strings/
# class Solution:
#     def buddyStrings(self, A: str, B: str) -> bool:
def buddyStrings(A, B):
    if len(A) != len(B):
        print("1st if")
        return False
    # if set(A) == set(B) and A != B:
    #     print("2nd if")
    #     return True
    if set(A) == set(B) and len(set(A)) == 1:
        print("3rd if")
        return True
    b_i_l = [i for i in range(len(B))]
    count = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            b_i_l.remove(i)
        elif A[i] in B:
            count += 1
            b_i_l.remove(i)
        else:
            return False
    if count == 0:
        return True
    else:
        return False

# assert(buddyStrings(A = "ab", B = "ba")) == True
# assert(buddyStrings(A = "ab", B = "ab")) == False
# assert(buddyStrings(A = "aa", B = "aa")) == True
print(buddyStrings("abcd", "badc"))