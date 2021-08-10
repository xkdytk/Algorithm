answer = -1

def DFS(n, pos, num, number, s):
    global answer
    if pos > 8:
        return
    if num == number:
        if pos < answer or answer == -1:
            print(s)            
            answer=pos
        return

    nn=0
    for i in range(8):
        nn=nn*10+n
        DFS(n, pos+1+i, num+nn, number, s+'+')
        DFS(n, pos+1+i, num-nn, number, s+'-')
        DFS(n, pos+1+i, num*nn, number, s+'*')
        DFS(n, pos+1+i, num/nn, number, s+'/')

def solution(N, number):    
    DFS(N, 0, 0, number, '')    
    return answer

# 재귀를 사용하여 해결한 방법 (내 해결 방법보다 시간이 오래 걸림)

print(solution(5, 12))
print(solution(2, 11))