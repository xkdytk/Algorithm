def solution(citations):
    answer = 0
    temp = [0] * (max(citations)+1)
    h_index = []

    for i in citations:
        for j in range (i+1):
            temp[j] += 1
        
    for i in range(len(temp)):
        if i <= temp[i]:
            h_index.append(i)

    answer = max(h_index)

    return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([0, 0, 0, 0, 1]))
print(solution([6, 5, 4, 1, 0]))