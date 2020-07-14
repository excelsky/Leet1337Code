# https://leetcode.com/problems/angle-between-hands-of-a-clock/
# class Solution:
#     def angleClock(self, hour: int, minutes: int) -> float:
def angleClock(hour, minutes):
    min_angle = 6 * minutes
    if hour == 12:
        hr_angle = 0
    else:
        hr_angle = 30 * hour
    hr_angle += minutes / 2        
    ans = abs(min_angle - hr_angle)
    return min(ans, 360-ans)

assert(angleClock(12,30)) == 165
assert(angleClock(3,30)) == 75
assert(angleClock(3,15)) == 7.5