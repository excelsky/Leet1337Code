# def return_filled_array(input_lst):
#     if input_lst is None:
#         return None
#     output_lst = []
#     if input_lst == []:
#         return output_lst
#     for i in range(len(input_lst)):
#         if i > 0 and input_lst[i] is None:
#             if input_lst[i-1] is not None:
#                 output_lst.append(input_lst[i-1])
#             else:
#                 output_lst.append(output_lst[i-1])
#         else:
#             output_lst.append(input_lst[i])
#     return output_lst


def return_filled_array(input_lst):
    if input_lst is None or len(input_lst) <= 1:  # It is important to have "is None" condition first
        return input_lst
    output_lst = input_lst[:]
    for i in range(1, len(input_lst)):
        if input_lst[i] is None and output_lst[i-1] is not None:
            output_lst[i] = output_lst[i-1]
    return output_lst

assert return_filled_array([]) == []
assert return_filled_array(None) == None
assert return_filled_array([None, 1]) == [None, 1]
assert return_filled_array([2, None, 3]) == [2, 2, 3]
assert return_filled_array([4, None, 5, None, None, 6]) == [4, 4, 5, 5, 5, 6]