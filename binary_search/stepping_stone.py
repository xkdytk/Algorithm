def solution(distance, rocks, n):
    answer = 0
    
    left = 1
    right = distance

    rocks.extend([0, distance])

    rocks.sort()

    while left <= right:
        rm = 0
        dis = []
        mid = (left + right) // 2

        for i in range(len(rocks)-1):
            dis.append(rocks[i+1] - rocks[i])

        for i in range(len(dis)-1):
            
            if dis[i] < mid:
                rm += 1
                dis[i+1] += dis[i]

        if rm <= n:
            if answer < mid:
                answer = mid   # 전에 찾았던 최대값보다 더 큰 최대값을 찾으면 그것으로 대체
            left = mid + 1
        else:
            right = mid - 1

        # else:
        #    answer = mid
        #    break
        # 처음에 이렇게 풀었는데 풀리지 않았다. 이는 문제에 문제가 있었던 것같다. 
        # n개 제거할때를 가정하고 풀이하니까 틀렸다고 처리되었고 n개 이하로 제거하는 방식으로 전개하니까 정답처리되고 
        
    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))
print(solution(16, [4, 8, 11], 2))