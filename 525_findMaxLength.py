# def findMaxLength(self, nums: List[int]) -> int:
def findMaxLength(nums):
    dic = {0:-1}
    count = 0
    maxlen = 0
    for i in range(len(nums)):
        print("\ni", i)
        print(1 if nums[i] == 1 else -1)
        print("count", count)
        count += (1 if nums[i] == 1 else -1)
        print("count", count)
        if count in dic:
            print("i", i)
            print("dic[count]", dic[count])
            print("i - dic[count]", i - dic[count])
            print("maxlen", maxlen)
            maxlen = max(maxlen, i - dic[count])
            print("maxlen", maxlen)
        else:
            dic[count] = i
            print("dic", dic)
    return maxlen

input0 = [0,1]
output0 = 2
input1 = [0,1,0]
output1 = 2
input2 = [1,2,1,2]
output2 = 4

print("\n***assert0")
assert findMaxLength(input0) == output0
print("\n***assert1")
assert findMaxLength(input1) == output1
print("\n***assert2")
assert findMaxLength(input2) == output2