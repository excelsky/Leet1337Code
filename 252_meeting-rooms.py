# https://leetcode.com/problems/meeting-rooms
# class Solution:
#     def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
def canAttendMeetings(intervals):
    intervals.sort()
    for i in range(len(intervals)-1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
    return True


intervals = [[0,30],[5,10],[15,20]]
assert(canAttendMeetings(intervals) == False)

intervals = [[7,10],[2,4]]
assert(canAttendMeetings(intervals) == True)