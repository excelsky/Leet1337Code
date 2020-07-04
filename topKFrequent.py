import collections, heapq


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """ 
    C = collections.Counter(nums)   
    # return heapq.nlargest(k, C.keys(), key=C.get) 
    x = C.most_common(k)
    return [i[0] for i in x]


'''
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''