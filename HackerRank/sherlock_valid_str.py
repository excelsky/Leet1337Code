import collections

def isValid(s):
    str_C = collections.Counter(s)
    # print("str_C", str_C)
    freq_C = collections.Counter(str_C.values())
    # print("freq_C", freq_C)
    if len(freq_C) == 1:
        return "YES"
    elif len(freq_C) > 2:
        return "NO"
    else:
        freq_key_list = list(freq_C.keys())
        freq_value_list = list(freq_C.values())
        # print("freq_key_list", freq_key_list)
        # print("freq_value_list", freq_value_list)
        if freq_C[1] == 1:
            return "YES"
        elif abs(freq_key_list[0] - freq_key_list[1]) > 1:
            return "NO"
        elif 1 in freq_value_list:
            return "YES"
        else:
            return "NO"

s = "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"
assert isValid(s) == "YES"