def solution(enter, leave):
    answer = [0] * len(enter)

    room = []
    e_idx = 0
    for l in leave:
        while l not in room:
            room.append(enter[e_idx])
            e_idx += 1
        room.remove(l)
        for p in room:
            answer[p - 1] += 1
        answer[l - 1] += len(room)

    return answer

# 비슷한 방법으로 해결