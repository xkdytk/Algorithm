def solution(participant, completion):
    answer = ''
    dic = {}

    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in completion:
        if i in dic:
            dic[i] -= 1

    for i in participant:
        if dic[i] > 0:
            answer = i

    return answer

participant_1 = ["leo", "kiki", "eden"]
completion_1 = ["eden", "kiki"]

participant_2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion_2 = ["josipa", "filipa", "marina", "nikola"]

participant_3 = ["mislav", "stanko", "mislav", "ana"]
completion_3 = ["stanko", "ana", "mislav"]

print(solution(participant_1, completion_1))
print(solution(participant_2, completion_2))
print(solution(participant_3, completion_3))