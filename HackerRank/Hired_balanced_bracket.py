# def solution(angles):
#     # Type your solution here
#     if len(angles) > 1:
#         print("if")
#         new_angles = []
#         for i in range(len(angles)-1):
#             print(i)
#             if (angles[i] != "<" or angles[i+1] != ">") and i+2 == len(angles):
#                 print("ifif")
#                 new_angles.append(angles[i])
#                 new_angles.append(angles[i+1])
#             elif angles[i] != "<" or angles[i+1] != ">":
#                 print("elif")
#                 new_angles.append(angles[i])
                
#     else:
#         print("else")
#         new_angles = list(angles)
#     print(new_angles)
#     left_cnt = new_angles.count("<")
#     right_cnt = new_angles.count(">")
#     print(left_cnt)
#     print(right_cnt)
#     ans = right_cnt * "<" + angles + left_cnt * ">"
#     return ans


# def solution(angles):
#     # Type your solution here
#     bal_cnt = 0
#     left_cnt = 0
#     right_cnt = 0
#     for i in range(len(angles)):
#         if angles[i] == "<":
#             bal_cnt += 1
#             left_cnt += 1
#         else:
#             bal_cnt -= 1
#             right_cnt += 1

# #         if balance == -1:
# #             balance += 1
# #             left_cnt += 1
# #             ans += 1
#     print(bal_cnt)
#     print(left_cnt)
#     print(right_cnt)
#     ans = right_cnt * "<" + angles + left_cnt * ">"
#     return ans
    

def solution(angles):
    # Type your solution here
    left_cnt = 0
    right_cnt = 0
    for i in range(len(angles)):
        if angles[i] == "<":
            left_cnt += 1
        else:
            right_cnt += 1

    diff = min(left_cnt, right_cnt) - 1
    if diff == -1:
        diff = 0
    to_right_cnt = left_cnt - diff
    to_left_cnt = right_cnt - diff
    ans = to_left_cnt * "<" + angles + to_right_cnt * ">"
    return ans


angles = "<<>>>>><<<>>"
my_output = "<<<<<<<<<>>>>><<<>>>>>>>"
output = "<<<<<>>>>><<<>>>"
assert(solution(angles)) == output


angles = ">"
output = "<>"
assert(solution(angles)) == output


angles = ">>"
output = "<<>>"
assert(solution(angles)) == output

angles = "><<><"
output = "<><<><>>"
assert(solution(angles)) == output