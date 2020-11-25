# https://leetcode.com/problems/basic-calculator-ii
# 6gaksu

class Solution:
    def calculate(self, s: str) -> int:
        num, op, stack = 0, '+', [0]
        ops = {'+':lambda x, y: y, '-':lambda x, y: -y, '*':lambda x, y: x*y, '/':lambda x, y: (int)(float(x)/float(y))}
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() and c != ' ' or i == len(s)-1:
                prev = 0 if op in '+-' else stack.pop()
                stack.append(ops[op](prev, num))
                num, op = 0, c
        return sum(stack)