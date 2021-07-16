import heapq

def solution(jobs):
    answer = 0
    total = 0
    len_jobs = len(jobs)
    possible = []
    heapq.heapify(jobs)

    while len(jobs):

        while jobs[0][0] <= total:
            point, time = heapq.heappop(jobs)
            heapq.heappush(possible, [time, point])
            if len(jobs) == 0:
                break

        if len(possible):
            time, point = heapq.heappop(possible)
            total += time
            answer += total - point
        else:
            total += 1

    while len(possible):

        time, point = heapq.heappop(possible)
        total += time
        answer += total - point

    answer /= len_jobs

    return int(answer)

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))