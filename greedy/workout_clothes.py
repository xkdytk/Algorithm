def solution(n, lost, reserve):
    answer = 0

    lost_1 = list(set(lost) - set(reserve))
    reserve_1 = list(set(reserve) - set(lost))

    answer += n - len(lost_1)

    while reserve_1:
        if not lost_1:
            break
        
        tmp = reserve_1.pop(0)

        if lost_1.count(tmp-1) == 1:
            lost_1.remove(tmp-1)
            answer += 1

        elif lost_1.count(tmp+1) == 1:
            lost_1.remove(tmp+1)
            answer += 1

    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(10, [8,10], [6,7,9]))
print(solution(5, [2, 3, 4], [3, 4, 5]))