def solution(enter, leave):
    answer = [0] * len(enter)
    meeting = []
    enter_idx, leav_idx = 0, 0

    while enter_idx < len(enter) or leav_idx < len(leave):
        if leave[leav_idx] in meeting:
            meeting.remove(leave[leav_idx])
            leav_idx += 1
        else:
            for i in meeting:
                answer[i-1] += 1
            answer[enter[enter_idx]-1] += len(meeting)
            meeting.append(enter[enter_idx])
            enter_idx += 1
    return answer

print(solution([1,3,2], [1,2,3]))
print(solution([1,4,2,3], [2,1,3,4]))
print(solution([3,2,1], [2,1,3]))
print(solution([3,2,1], [1,3,2]))
print(solution([1,4,2,3], [2,1,4,3]))