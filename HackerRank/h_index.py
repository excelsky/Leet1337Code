def h_index(citation_list):
    citation_list.sort()
    n = len(citation_list)
    for index, element in enumerate(citation_list):
        if n-index <= element:
            return n-index
    return 0


    

if __name__ == "__main__":
    input_string = input("Enter integers separated by space: ")
    str_list = input_string.split()
    int_list = []
    for s in str_list:
        int_list.append(int(s))

    ans = h_index(int_list)
    print(ans)