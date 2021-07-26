from itertools import permutations
from math import sqrt

def solution(numbers):
    answer = 0
    arr = []

    for i in range(1,len(numbers)+1):
        arr += permutations(list(numbers), i)

    for i in range(len(arr)):
        arr[i] = int("".join(arr[i]))
    
    arr = list(set(arr))

    if arr.count(0) == 1:
        arr.remove(0)

    if arr.count(1) == 1:
        arr.remove(1)

    for i in arr:
        decimal = True
        num = int(sqrt(i))
        for j in range (2, num+1):
            if i % j == 0:
                decimal = False
                break
        if decimal == True:
            answer += 1

    return answer

print(solution("17"))
print(solution("011"))