def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for i in range (n+1)]

    for i in range (1, m+1):
        for j in range (1, n+1):
            if i == 1 and j == 1:
                dp[1][1] = 1
            elif [i, j] in puddles:
                dp[j][i] = 0
            else:
                dp[j][i] = dp[j][i-1] + dp[j-1][i]
            
    answer = dp[n][m] % 1000000007

    return answer

print(solution(4, 3, [[2, 2]]))