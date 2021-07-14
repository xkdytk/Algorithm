from collections import deque

def solution(prices):
    answer = []
    prices = deque(i for i in prices)

    while len(prices):
        present = prices.popleft()
        drop_check = False

        time = 0

        for i in prices:
            time += 1
            if i < present:
                answer.append(time)
                drop_check = True
                break
        
        if drop_check == False:
            answer.append(time)
            
    return answer

print(solution([1, 2, 3, 2, 3]))
print(solution([1, 2, 3, 2, 3, 1]))