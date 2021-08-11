def solution(triangle):
    triangle = [[0] + line + [0] for line in triangle]
    
    for i in range(1, len(triangle)):
        for j in range(1, i+2):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            print(triangle)
            
    return max(triangle[-1])


#          [0, 7, 0]
#       [0, 10, 15, 0]
#     [0, 18, 16, 15, 0]
#   [0, 20, 25, 20, 19, 0]
# [0, 24, 30, 27, 26, 24, 0]]

# 예외처리 계산이 편하게 허깨비 세우면 편하다.
# triangle = [[0] + line + [0] for line in triangle]
