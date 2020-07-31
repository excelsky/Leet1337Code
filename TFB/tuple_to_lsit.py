def solution(array):
    # print(array)
    liste = str(array).split()
    # print(liste)
    return [int(i) for i in liste[0]]


assert solution(123) == [1,2,3]
assert solution(400) == [4,0,0]
# solution((123))