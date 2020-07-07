# https://leetcode.com/problems/island-perimeter/
# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
def islandPerimeter(grid):
    ans = 0
    for row in range(len(grid)):
        for element in range(len(grid[row])):
            if grid[row][element] == 1:
                ans += 4
                if element > 0 and grid[row][element-1] == 1:
                    ans -= 2
                if row > 0 and grid[row-1][element] == 1:
                    ans -= 2
    return ans


grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

assert(islandPerimeter(grid)) == 16