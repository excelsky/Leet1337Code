'''
Q: given a list of tuples of movie watched times,
find how many unique minutes of the movie did the viewer watch
e.g. [(0,15),(10,25)]. The viewer watched 25 minutes of the movie
'''
t = [(0, 10), (15, 25), (12, 20), (30, 48)]
t.sort()

tol = t[0][1] - t[0][0]

for i in range(len(t) - 1):
    if t[i][1] > t[i+1][0]:
        tol += t[i+1][1] - t[i][1]
    else:
        tol += t[i+1][1] - t[i+1][0]
print(tol)