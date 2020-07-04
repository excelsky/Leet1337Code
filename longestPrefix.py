def longestPrefix(s):
    print(len(s))
    if len(s) == 1:
        return ""
    else:
        prefix_list = []
        suffix_list = []
        for i in range(2, len(s)+1):
            print(i)
            print(s[0:i])
            print(s[-i+1:])
            prefix_list.append(s[0:i])
            suffix_list.append(s[-i+1:])
        print(set(prefix_list))
        print(set(suffix_list))
        return set(prefix_list) & set(suffix_list)
    