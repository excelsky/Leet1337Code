import collections

# def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
def arraysIntersection(arr1, arr2, arr3):
    C = collections.Counter(arr1 + arr2 + arr3)
    return list(filter(lambda x : C[x] == 3, C.keys()))

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
output = [1,5]

assert arraysIntersection(arr1, arr2, arr3) == output