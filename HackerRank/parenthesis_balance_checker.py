def splitter(parentheses):
    list_parentheses = list(parentheses)
    len_list_parentheses = len(list_parentheses)
    dict_parentheses = {"(": ")", "{": "}", "[": "]"}
    if len_list_parentheses % 2 == 1:
        print("not balanced")
        return "not balanced"
    else:
        for i in range(len_list_parentheses // 2):
            if list_parentheses[i] not in dict_parentheses:
                print("not balanced")
                return "not balanced"
            elif dict_parentheses[list_parentheses[i]] != list_parentheses[-i-1]:
                    print("not balanced")
                    return "not balanced"
        print("balanced")
        return "balanced"

    

if __name__ == "__main__":
    # example_input = '{([])}'
    example_input = '([]'
    splitter(example_input)
    # print(simple())
