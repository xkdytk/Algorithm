def solution(number, k):
    answer = ''
    num = list(number)

    for i in num:

        while answer and answer[-1] < i and k > 0:
            answer = answer[:-1]
            k -= 1

        answer += i

    if k != 0:
        answer = answer[:-k]
    
    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("321924", 2))
print(solution("99991", 3))
print(solution("111119", 3))