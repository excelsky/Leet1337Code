# https://leetcode.com/problems/iterator-for-combination
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.k = combinationLength
        self.chars = characters
        
        # init the first combination
        self.nums = list(range(self.k))
        self.has_next = True
        
    def next(self) -> str:
        nums = self.nums
        n, k = self.n, self.k
        curr = [self.chars[j] for j in nums]
        
        # Generate next combination.
        # Find the first j such that nums[j] != n - k + j.
        # Increase nums[j] by one.
        j = k - 1
        while j >= 0 and nums[j] == n - k + j:
            j -= 1 
        nums[j] += 1
        
        if j >= 0:
            for i in range(j + 1, k):
                nums[i] = nums[j] + i - j
        else:
            self.has_next = False
        
        return ''.join(curr)
        
    def hasNext(self) -> bool:
        return self.has_next
        

characters = "abc"
combinationLength = 2
# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator(characters, combinationLength)
param_1 = obj.next()
param_2 = obj.hasNext()