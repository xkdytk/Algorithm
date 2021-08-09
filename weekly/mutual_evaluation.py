import numpy as np

def solution(scores):
    answer = ''
    grades = []
    scores = np.array(scores)
    for i in range (len(scores)):
        score = scores[:,i]
        
        if (score[i] == np.max(score)) & (np.count_nonzero(score == np.max(score)) == 1):
            score = np.delete(score, np.argmax(score))
        elif (score[i] == np.min(score)) & (np.count_nonzero(score == np.min(score)) == 1):
            score = np.delete(score, np.argmin(score))

        grades.append(score)
    
    for grade in grades:
        tmp = grade.mean()
        if tmp >= 90:
            answer += 'A'
        elif tmp >= 80:
            answer += 'B'
        elif tmp >= 70:
            answer += 'C'
        elif tmp >= 50:
            answer += 'D'
        else:
            answer += 'F'
    
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))