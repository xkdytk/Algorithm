def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossing = [0 for i in range (bridge_length)]
    
    while len(truck_weights) > 0:
        wait = truck_weights[0]
        crossing.pop(0)

        if wait + sum(crossing) <= weight:
            crossing.append(truck_weights.pop(0))
        else:
            crossing.append(0)
        answer += 1

    if len(crossing) > 0:
        answer += bridge_length

    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))