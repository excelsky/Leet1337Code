def solution(array):
    ans = []
    for i in range(len(array)):
        if i % 2 == 1:
             ans.append(array[i])
    return ans


assert solution([0,1,2,3,4,5]) == [1,3,5]
assert solution([1,-1,2,-2]) == [-1,-2]