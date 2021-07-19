import heapq

def solution(operations):
    answer = []

    while len(operations):
        op, num = operations.pop(0).split()

        if op == "I":
            heapq.heappush(answer,(int(num)))
        else:
            if len(answer) == 0:
                    continue
            elif num == "1":
                for i in range (len(answer)):
                    answer[i] = -answer[i]

                heapq.heapify(answer)
                heapq.heappop(answer)

                for i in range (len(answer)):
                    answer[i] = -answer[i]

                heapq.heapify(answer)
            
            else:
                heapq.heappop(answer)

    if len(answer) == 0:
        return [0,0]

    else:
        return [max(answer),min(answer)]

print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 2","I 4","D -1", "I 1", "D 1"]))