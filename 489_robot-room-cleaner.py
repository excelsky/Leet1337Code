# https://leetcode.com/problems/robot-room-cleaner
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def dfs(robot, i, j, d, cleaned):
            robot.clean()
            cleaned.add((i,j))
            left = True
            for nd in ((d+k) % 4 for k in (3,0,1,2)):
                robot.turnLeft() if left else robot.turnRight()
                di, dj = ((-1,0),(0,1),(1,0),(0,-1))[nd]
                if (i+di, j+dj) not in cleaned and robot.move():
                    dfs(robot, i+di, j+dj, nd, cleaned)
                    robot.move()
                    left = True
                else:
                    left = False
        dfs(robot, 0, 0, 0, set())
        