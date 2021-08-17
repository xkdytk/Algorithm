def solution(n, computers):
    answer = 0

    check = [0] * n

    for i in range(n):
        if check[i] == 0:
            DFS(check,i, computers, n)
            answer += 1

    return answer

def DFS(check, idx, computer, n):
    check[idx] = 1
    for i in range(n):
        if i != idx and computer[idx][i] == 1 and check[i] == 0:
            DFS(check, i, computer, n)


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))