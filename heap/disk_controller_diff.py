import heapq

def solution(jobs):
    answer = 0
    
    wait_list = []
    count = 0
    clock = -1
    n = len(jobs)
    now_time = 0

    while count < n:
        for job in jobs:
            if clock < job[0] <= now_time:
                answer += (now_time - job[0])
                heapq.heappush(wait_list,job[1])
        if len(wait_list) > 0:
            answer += len(wait_list)*wait_list[0]
            clock = now_time
            now_time += heapq.heappop(wait_list)
            count += 1
        else:
            now_time += 1
    
    return answer//n

# clock을 이용해서 실제로 시간이 진행되는 것으로 구현