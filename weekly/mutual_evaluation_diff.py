from collections import Counter
def solution(scores):   
    answer = ''

    print(list(map(list, zip(*scores))))

    for idx, score in enumerate(list(map(list, zip(*scores)))):
        length = len(score)
        if Counter(score)[score[idx]] == 1 and (max(score) == score[idx] or min(score) == score[idx]):
            del score[idx]
            length -= 1

        grade = sum(score) / length

        if grade >= 90:
            answer += 'A'
        elif grade >= 80:
            answer += 'B'
        elif grade >= 70:
            answer += 'C'
        elif grade >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer

# Counter 모듈을 사용해서 해결한 방법

# zip(*scores) 여기서 별표(*)는 리스트의 원소를 개별적인 입력인자로 zip() 함수에 넘겨주는 역할을 합니다.
# 2차원 배열과 관련해서 열(=col)들을 가져올때 zip을 사용하면 유용하다.


print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))