def return_mismatched(str1, str2):
    # Code here
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = []
    for s in set1:
        if s not in set2:
            ans.append(s)
    for s in set2:
        if s not in set1:
            ans.append(s)
    return ans


def cmp_lst(l1,l2):
    return sorted(l1) == sorted(l2)


assert cmp_lst(return_mismatched("",""), []) == True
assert cmp_lst(return_mismatched("","This is the second string"), ['This','is','the','second','string']) == True
assert cmp_lst(return_mismatched("This is the first string",""), ['This','is','the','first','string']) == True
assert cmp_lst(return_mismatched("This is the first string","This is the second string"),['first', 'second']) == True
assert cmp_lst(return_mismatched("This is the first string extra","This is the second string"),['first', 'second', 'extra']) == True
assert cmp_lst(return_mismatched("This is the first text","This is the second string"),['first', 'text', 'second', 'string']) == True
assert cmp_lst(return_mismatched("Firstly this is the first string","Next is the second string"), ['Firstly', 'this', 'first', 'Next', 'second']) == True
print('passed')