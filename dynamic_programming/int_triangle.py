def solution(triangle):
    answer = 0

    for index in range(1, len(triangle)):
        for j in range(len(triangle[index])):
            if j == 0:
                triangle[index][j] += triangle[index-1][j]
            elif j == len(triangle[index])-1:
                triangle[index][j] += triangle[index-1][j-1]
            else:
                triangle[index][j] += max(triangle[index-1][j-1], triangle[index-1][j])

    answer = max(triangle[len(triangle)-1])

        
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

