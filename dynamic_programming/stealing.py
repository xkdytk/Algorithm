def solution(money):
    dp = [money[0], money[0]]
    dp2 = [0, money[1]]

    for i in range(2, len(money)-1):
        dp.append(max(dp[i-2] + money[i], dp[i-1]))

    for i in range(2, len(money)):
        dp2.append(max(dp2[i-2] + money[i], dp2[i-1]))

    return max(dp[-1], dp2[-1])

print(solution([1, 2, 3, 1]))
print(solution([1, 1, 4, 1, 4])) # 8
print(solution([1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000])) # 3000
print(solution([1, 5, 1, 5, 1])) # 10
print(solution([91, 90, 5, 7, 5, 7])) # 104
print(solution([90, 0, 0, 95, 1, 1])) # 185
