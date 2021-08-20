def solution(n, times):
    answer = 0
    left = 1
    right = n * max(times)

    while left <= right:
        mid = (left + right) // 2
        total = 0

        for i in times:
            total += mid // i

        if total >= n:
            answer = mid
            right = mid -1
        else:
            left = mid + 1
    return answer

print(solution(6, [7, 10]))