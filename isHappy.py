def isHappy(n):
    if n < 10 and n > 1:
        return False
    while n >= 10:
        liszt = list(str(n))
        n = sum([int(i)**2 for i in liszt])
    if n == 1:
        return True
    else:
        return False