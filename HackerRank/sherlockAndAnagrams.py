#!/bin/python3

from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)+1):
        print("\n")
        print("i", i)
        print("len(s)-i+1", len(s)-i+1)
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        print("a", a)
        b = Counter(a)
        print("b", b)
        for j in b:
            print("j", j)
            count+=b[j]*(b[j]-1)/2
            print(count)
    return int(count)

if __name__ == '__main__':
    s = "cdcd"
    result = sherlockAndAnagrams(s)
    result