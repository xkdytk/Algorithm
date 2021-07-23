def solution(answers):
    answer = []
    score = [0] * 3
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range (len(answers)):
        if answers[i] == first[i%5]:
            score[0] += 1
        if answers[i] == second[i%8]:
            score[1] += 1
        if answers[i] == third[i%10]:
            score[2] += 1

    for i in range (len(score)):
        if score[i] == max(score):
            answer.append(i+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))