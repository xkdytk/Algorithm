from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)])
    while queue:
        sum, idx = queue.popleft()
        if idx > len(numbers):
            break
        elif idx == len(numbers) and sum == target:
            answer += 1
        queue.append((sum+numbers[idx-1], idx+1))
        queue.append((sum-numbers[idx-1], idx+1))

    return answer

print(solution([1, 1, 1, 1, 1],3))