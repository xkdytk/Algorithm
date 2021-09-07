def solution(word):
    answer = 0
    dic = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    num = [781, 156, 31, 6, 1]

    for index, element in enumerate (word):
        answer += dic[element]*num[index]+1

    return answer

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))