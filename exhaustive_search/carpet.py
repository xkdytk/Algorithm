from math import sqrt

def solution(brown, yellow):
    answer = []

    total = brown + yellow

    for i in range (1, int(sqrt(total))+1):
        if total % i == 0:
            if int(total/i-2) * (i-2) == yellow:
                answer.append(int(total/i))
                answer.append(i)

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))