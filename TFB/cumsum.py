def solution(array):
    ans = []
    for i in range(len(array)):
        ans.append(array[i])
        if i > 0:
            ans[i] += ans[i-1]
    return ans


assert solution([1,1,1]) == [1,2,3]
assert solution([1,-1,3]) == [1,0,3]
