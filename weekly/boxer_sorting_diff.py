def solution(weights, head2head):
    result = []
    l = len(weights)
    # 한 번에 정렬해서 풀어봅시다!
    ans = [[0 for _ in range(4)] for _ in range(l)] # 승률, 무거운복서 이긴횟수, 자기 몸무게, 번호(음수로)
    for i in range(l):
        ans[i][2] = weights[i]
        ans[i][3] = -(i+1)
        cnt = 0 # 판수
        for j in range(l):
            if head2head[i][j] == 'W':
                ans[i][0] += 1 # 일단 이김
                cnt += 1
                if weights[i] < weights[j]:
                    ans[i][1] += 1 # 무거운 복서 이김
            elif head2head[i][j] == 'L':
                cnt += 1 # 판수만 늘려준다
        if cnt == 0:
            ans[i][0] = 0
        else:
            ans[i][0] /= cnt
    ans.sort(reverse=True) # 역순으로 정렬하면 모든 조건이 한 번에 정렬된다

    for i in range(l):
        result.append(-ans[i][3])
    return result

# 파이썬 리스트는 정렬하면 내부 요소의 순서대로 정렬이 되는것을 이용해 굳이 람다식으로 4중 정렬을 안해도 됌
# 내림차순으로 정렬하는 문제인데 번호만 유일하게 작은순으로 정렬하는 것이여서 이는 음수 처리