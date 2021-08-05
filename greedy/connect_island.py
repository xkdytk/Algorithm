def solution(n, costs):
    answer = 0
    
    costs.sort(key = lambda x : x[2])

    path = set([costs[0][0]])

    while len(path) != n:
        for i, cost in enumerate(costs):
            if cost[0] in path and cost[1] in path:
                continue
            if cost[0] in path or cost[1] in path:
                path.update([cost[0], cost[1]])
                answer += cost[2]
                costs[i] = [-1, -1, -1]
                break

    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])) # 11