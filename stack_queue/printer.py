def solution(priorities, location):
    answer = 0
    index = [i for i in range(len(priorities))]

    while len(priorities) > 0 :
        have_large = False
        compar = priorities.pop(0)

        for i in range (len(priorities)):
            if priorities[i] > compar:
                priorities.append(compar)
                index.append(index.pop(0))
                have_large = True
                break

        if have_large == True:
            continue
        else:
            answer += 1
            if (index.pop(0) == location):
                break
            

    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))