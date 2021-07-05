import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
# collections.Counter를 이용해 dictionary끼리 연산하여 완주하지 못한 한 명을 찾아내는 코드입니다.

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
# dictionary 내부에서 빠르게 찾기 위해 hash 함수를 사용한 코드입니다.