def dfs(begin, target, words, visit):
    answer = 0
    stacks = [begin]
    while stacks:
        stack = stacks.pop() # 리스트의 마지막 부분을 뺌 (DFS)
        if stack == target:
            return answer
        
        for i in range(len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != stack[j]]) == 1:
                
                if visit[i] != 0:
                    continue
                visit[i] = 1
                stacks.append(words[i])
        answer += 1
    return answer

def solution(begin, target, words):
    if target not in words:
        return 0
    visit = [0 for i in words] # 깊이 우선 탐색이기 때문에 방문 기록을 남겨야함
    answer = dfs(begin, target, words, visit)

    return answer
    
# ​DFS를 이용한 문제 해결