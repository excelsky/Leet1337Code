def solution(arr):
    # Type your solution here
    if len(arr) <= 1:
        return ""
    
    new_arr = []
    for a in arr:
        if a >= 0:
            new_arr.append(a)

    n = len(new_arr)        
    possible_left_indices = [(i+1) * (i+2) // 2 for i in range(n)]

    left_indices = []
    right_indices = []
    for i in possible_left_indices:
        if i < n:
            left_indices.append(i)
            if i-1 > 0:
                right_indices.append(i-1)
        elif i == n:
            right_indices.append(i-1)
    
    left_sum = sum(list(new_arr[i] for i in left_indices))
    right_sum = sum(list(new_arr[i] for i in right_indices))
    
    if left_sum > right_sum:
        return "Left"
    elif left_sum < right_sum:
        return "Right"
    else:
        return ""