import math

def solution(arr):
    # Type your solution here
    n = len(arr)
    if n <= 1:
        return n

    left_indices = [2**i-1 for i in range(math.floor(math.log2(n))+1) if 2**i-1 < n]
    right_indices = [2**i-2 for i in range(1, math.floor(math.log2(n))+2) if 2**i-2 < n]
    # print("left_indices", left_indices)
    # print("right_indices", right_indices)

    left_list = list(arr[i] for i in left_indices)
    right_list = list(arr[i] for i in right_indices)

    left_height = len(left_list) - left_list.count(-1)
    right_height = len(right_list) - right_list.count(-1)

    return max(left_height, right_height)



arr = [1, -1, 1, -1, -1, -1, 1]
arr = [1,1,1,1]
solution(arr)