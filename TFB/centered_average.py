def solution(array):
    array.sort()
    array.pop()
    array.remove(min(array))
    return sum(array) // len(array)


assert solution([1, 2, 3, 4, 100]) == 3
assert solution([1, 1, 5, 5, 10, 8, 7]) == 5
assert solution([-10, -4, -2, -4, -2, 0]) == -3