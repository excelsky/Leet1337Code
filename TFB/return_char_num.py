# def return_char_num(input_str, char):
#     if len(input_str) == 0:
#         return 0
#     d = {}
#     for i in input_str:
#         if i not in d.keys():
#             d[i] = 1
#         else:
#             d[i] += 1
#     return d[char]

# assert return_char_num("", "") == 0
# assert return_char_num("hello", "h") == 1
# assert return_char_num("mississipi", "s") == 4


# def return_char_num(input_str, char):
#     if len(input_str) == 0:
#         return 0
#     count = 0
#     for i in input_str:
#         if i == char:
#             count += 1
#     return count

# assert return_char_num("", "") == 0
# assert return_char_num("hello", "h") == 1
# assert return_char_num("mississipi", "s") == 4



def return_char_num(input_str, char):
    if len(input_str) == 0:
        return 0
    return input_str.count(char)
assert return_char_num("", "") == 0
assert return_char_num("hello", "h") == 1
assert return_char_num("mississipi", "s") == 4

