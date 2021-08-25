from collections import deque

def solution(n, edge):
    answer = 0
    check = [0] * n
    adj = [[] for i in range(n)]
    for i in edge:
        adj[i[0]-1].append(i[1]-1)
        adj[i[1]-1].append(i[0]-1)
    
    queue = deque([[0, 0]])
    check[0] = 1
    alist = []

    while queue:
        start, depth = queue.popleft()
        
        for i in adj[start]:
            if check[i] == 0:
                queue.append([i, depth+1])
                alist.append(depth+1)
                check[i] = 1

    answer = alist.count(max(alist))

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))