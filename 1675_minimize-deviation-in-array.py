# https://leetcode.com/problems/minimize-deviation-in-array
# 6gaksu

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # pretreatment
        possible_list = []
        for num in nums:
            candidates = []
            if num % 2 == 0:
                temp = num
                candidates.append(temp)
                while temp % 2 == 0:
                    temp //= 2
                    candidates.append(temp)
            else:
                candidates.append(2*num)
                candidates.append(num)
            # reverse candidates to sort from small to large
            possible_list.append(candidates[::-1])

        pointers = [(candidates[0], i, 0)
                    for i, candidates in enumerate(possible_list)]

        heapq.heapify(pointers)
        min_deviation = inf
        current_end = max(candidates[0] for candidates in possible_list)
        # get minimum from heap
        while pointers:
            current_start, index, index_in_candidates = heapq.heappop(pointers)
            if current_end - current_start < min_deviation:
                min_deviation = current_end - current_start
            # if the pointer reach last
            if index_in_candidates + 1 == len(possible_list[index]):
                return min_deviation
            next_value = possible_list[index][index_in_candidates+1]
            current_end = max(current_end, next_value)
            heapq.heappush(pointers, (next_value, index, index_in_candidates+1))