# https://leetcode.com/problems/fizz-buzz
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
def fizzBuzz(n):
    fizz_buzz_d = {3 : "Fizz", 5 : "Buzz"}
    ans = []
    for i in range(n):
        fizz_buzz_s = ""
        for key in fizz_buzz_d.keys():
            if (i+1) % key == 0:
                fizz_buzz_s += fizz_buzz_d[key]
        if fizz_buzz_s == "":
            ans.append(str(i+1))
        else:
            ans.append(fizz_buzz_s)
    return ans

assert(fizzBuzz(1)) == ['1']
assert(fizzBuzz(15)) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']