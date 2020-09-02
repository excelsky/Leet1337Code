# https://leetcode.com/problems/contains-duplicate-iii
import collections
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
def containsNearbyAlmostDuplicate(nums, k, t):
    if k < 1 or t < 0:
        return False
    dic = collections.OrderedDict()
    for n in nums:
        key = n if not t else n // t
        for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
            if m is not None and abs(n - m) <= t:
                return True
        if len(dic) == k:
            dic.popitem(False)
        dic[key] = n
    return False


assert(containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0)) == True
assert(containsNearbyAlmostDuplicate(nums = [1,0,1,1], k = 1, t = 2)) == True
assert(containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3)) == False