# def checkValidString(self, s: str) -> bool:
def checkValidString(s):
    lo = hi = 0
    for c in s:
        lo += 1 if c == '(' else -1
        hi += 1 if c != ')' else -1
        if hi < 0: break  # Break when we have too many ")"
        lo = max(lo, 0)  # Reset lo to 0, if it is below 0
        print(lo, hi)
    return lo == 0

input0 = "(***)"
output0 = True
input1 = "(*))"
output1 = True
input2 = "())"
output2 = False

print("\nassert0")
print(input0)
assert checkValidString(input0) == output0
print("\nassert1")
print(input1)
assert checkValidString(input1) == output1
print("\nassert2")
print(input2)
assert checkValidString(input2) == output2