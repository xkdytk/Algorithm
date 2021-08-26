def solution(n, results):
    total = [['?' for i in range(n)] for j in range(n)]

    for i in range(n):
        total[i][i] = 'SELF'

    for result in results:
        total[result[0]-1][result[1]-1] = 'WIN'
        total[result[1]-1][result[0]-1] = 'LOSE'

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == 'WIN' and total[k][j] == 'WIN':
                    total[i][j] = 'WIN'
                elif total[i][k] == 'LOSE' and total[k][j] == 'LOSE':
                    total[i][j] = 'LOSE'

    answer = 0

    for i in total:
        if '?' not in i:
            answer += 1

    return answer

# Floyd-Warshell 알고리즘을 통해 해결

# Floyd-Warshell 알고리즘은 그래프가 Adjacency Matrix 형식으로 표현되었을 때 사용할 수 있는 알고리즘이다. 
# 따라서 입력 값을 Adjacency Matrix 형태의 그래프로 변환한다. 
# 구분을 위해 연결되지 않은 부분은 "?"", 이긴 쪽은 "WIN", 진 쪽은 "LOSE"로 구분했다.

# Floyd-Warshell 알고리즘의 기본적인 논리는 i점에서 j점을 갈 때 k 점을 거쳐 i -> k -> j로는 갈 수 있는가? 이다.
# i -> k 가 "LOSE"이고 k -> j 가 "LOSE"라면 이는 i가 k에게, k가 j에게 졌다는 것을 의미한다. 그렇다면 matrix[i][j]는 "Lose"가 된다. 또한 matrix[j][i]는 "True"가 된다. 
