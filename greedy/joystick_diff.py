def solution(name):
    length = len(name)
    answer = 0
    
    def alpha_count(char):
        table = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return table[ord(char) - ord('A')]
    
    for n in name:
        answer += alpha_count(n)
    
    move = length - 1
    for idx in range(length):
        next_idx = idx + 1
        while next_idx < length and name[next_idx] == 'A':
            next_idx += 1
        distance = min(idx, length-next_idx)
        move = min(move, idx+length-next_idx+distance)
    answer += move
    
    return answer

# 한 쪽 방향으로만 갔을 때 최적의 값이 나오면 좋겠지만 그렇지 않을 수 있다.

# 와리가리 했을 때 최적의 값이 나오는 경우를 대비해 모든 경우의 수를 검사해야한다. 
# 여기서는 for문을 이용해 이동한 오른쪽 끝이 0번째 인덱스일 경우부터 마지막 인덱스일 경우까지 모두 검사한다.

# idx는 오른쪽으로 간 횟수, length-next_idx는 왼쪽으로 간 횟수를 뜻한다. 
# 오른쪽과 왼쪽을 전부 방문하는 경우에는 한 쪽 방향을 선택한 뒤 돌아와야되는데, 이 때 횟수가 적은 방향을 먼저 선택해야한다. 
# 먼저 방문한 방향의 이동 횟수가 두배가 되니까(다시 돌아와야 하므로) 적은 방향을 선택해야 최솟값을 구할 수 있다.