def isBalanced(s):
    n = -1
    while len(s) != n:
        n = len(s)
        # print("\nn", n)
        s = s.replace('()', '')
        # print("s", s)
        s = s.replace('{}', '')
        # print("s", s)
        s = s.replace('[]', '')
        # print("s", s)
    # print("\ns", s)
    if len(s) == 0:
        return "YES"
    else:
        return "NO"



s_0 = "{[()]}"
s_1 = "{[(])}"
s_2 = "{{[[(())]]}}"

assert isBalanced(s_0) == "YES"
assert isBalanced(s_1) == "NO"
assert isBalanced(s_2) == "YES"