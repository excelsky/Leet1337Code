def minimumBribes(q):
    moves = 0
    q = [p-1 for p in q]
    print(q)
    for i,p in enumerate(q):
        print("i, p", i, p)
        if p - i > 2:
            return "Too chaotic"
        for j in range(max(p-1,0), i):
            print("j", j)
            print("q[j], p", q[j], p)
            if q[j] > p:
                moves += 1
                print(moves)
        print("\n")
    return moves


q = [1,2,5,3,7,8,6,4]
minimumBribes(q)