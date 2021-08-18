def solution(begin, target, words):
    answer = 0

    if target not in words:
        return answer

    queue = [(begin,0)]

    while queue:
        compar, idx = queue.pop(0)
        if compar == target:
            answer = idx
            break
        for i in words:
            if [c1 == c2 for c1, c2 in zip(compar, i)].count(False) == 1:
                queue.append((i, idx+1))
        
    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))