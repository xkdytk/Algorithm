def solution(routes):
    answer = 0
    index = 0
    routes.sort(key = lambda x : x[1])

    while index != len(routes):
        point = routes[index][1]
        if routes[index][0] == 30001:
             index += 1
             continue

        for i in range (index+1, len(routes)):
            if routes[i][0] == 30001:
                continue
            if point >= routes[i][0]:
                routes[i][0] = 30001

        answer += 1
        index += 1

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))
print(solution([[-2,-1], [1,2],[-3,0]])) #2
print(solution([[0,0],])) #1
print(solution([[0,1], [0,1], [1,2]])) #1
print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2