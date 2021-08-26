from collections import defaultdict

def solution(n, results):
    answer = 0
    wins = defaultdict(set) # key에게 진 사람들의 집합
    loses = defaultdict(set) # key에게 이긴 사람들의 집합

    for i, j in results:
        wins[i].add(j)
        loses[j].add(i)

    for i in range(1, n+1):
        for winner in loses[i]: # i에게 이긴 사람은 i에게 진 사람에게도 이긴다. 
            wins[winner].update(wins[i])

            # win[i] 대신 wins.get(i)를 통해 했더니 NoneType 에러가 발생했다.
            # 그 이유는 존재하지 않는 키(5)로 값을 가져오려고 할 경우 이와 같은 에러가 발생한다.
            # 반면 win[i]는 존재하지 않은 키의 값을 가져오라고 하면 set()처럼 빈 집합을 가져온다.

        for loser in wins[i]: # i에게 진 사람은 i를 이긴 사람에게도 진다.
            loses[loser].update(loses[i])

    for i in range(1, n+1):
        if len(wins.get(i)) + len(loses.get(i)) == n-1:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

 