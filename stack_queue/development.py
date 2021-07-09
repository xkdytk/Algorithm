def solution(progresses, speeds):
    answer = []
    finish = []
    for i in range (len(progresses)):
        if (100 - progresses[i])%speeds[i] > 0:
            finish.append(int((100 - progresses[i])/speeds[i]) + 1)
        else:
            finish.append(int((100 - progresses[i])/speeds[i]))
    
    while(len(finish) > 0):
        deploy = finish.pop(0)
        num = 1

        for i in finish:     
            if i > deploy:
                break
            else:
                num += 1

        for i in range(num-1):
            finish.pop(0)

        answer.append(num)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))