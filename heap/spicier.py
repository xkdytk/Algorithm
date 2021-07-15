import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        else:
            answer += 1
            min_1 = heapq.heappop(scoville)
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_1 + min_2*2)

    if scoville[0] < K:
        return -1
    else:
        return answer

print(solution([1, 2, 3, 9, 10, 12],7))