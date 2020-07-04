import collections

# def findJudge(self, N: int, trust: List[List[int]]) -> int:
def findJudge(N, trust):
    # if len(trust) == 1:
    #     return trust[0][1]
    # citizens = ""
    # judges = ""
    # for i in range(len(trust)):
    #     citizens += str(trust[i][0])
    #     judges += str(trust[i][1])
    # judge_d = collections.Counter(judges)
    # judge = judge_d.most_common(1)[0][0]
    # if judge in citizens:
    #     return -1
    # else:
    #     return int(judge)
    if len(trust) < N - 1:
        return -1

    trust_scores = [0] * (N + 1)

    for a, b in trust:
        trust_scores[a] -= 1
        trust_scores[b] += 1

    for i, score in enumerate(trust_scores[1:], 1):
        if score == N - 1:
            return i
    return -1


assert findJudge(2, [[1,2]]) == 2
assert findJudge(3, [[1,3],[2,3]]) == 3
assert findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3
assert findJudge(1, []) == 1