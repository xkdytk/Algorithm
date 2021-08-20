def solution(n, times):
    answer = 0
    # 최악의 경우: 가장 비효율적인 심사관에게 다 받는 경우의 시간.
    left, right = 1, max(times) * n

    while left <= right:
        # 한 심사관에게 주어진 시간
        mid = (left + right) // 2
        people = 0
        for i in times:
            # 각 심사관마다, 주어진 시간 동안 몇 명의 사람을 심사할 수 있는지
            people += mid // i
            # 모든 사람을 심사할 수 있으면 반복문을 벗어난다.
            if people >= n:
                break
        # 모든 사람을 심사할 수 있는 경우
        # 한 심사관에게 주어진 시간을 줄여본다
        if people >= n:
            answer = mid
            right = mid - 1
        # 모든 사람을 심사할 수 없는 경우
        # 한 심사관에게 주어진 시간을 늘려본다.
        elif people < n:
            left = mid + 1
    return answer

# 주석이 잘 달린 코드

def solution(n, times):
    answer = 0
    start, end, mid = 1, times[-1] * n, 0

    while start < end:
        mid = (start + end) // 2
        total = 0
        for time in times:
            total += mid // time

        if total >= n:
            end = mid
        else:
            start = mid + 1
    answer = start
    return answer

# 비슷한 코드