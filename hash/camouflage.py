def solution(clothes):
    answer = 1
    dic = {}

    for i in range(len(clothes)):
        dic[clothes[i][1]] = 0

    for i in range(len(clothes)):
        dic[clothes[i][1]] += 1
    
    for i in dic:
        answer *= dic.get(i)+1
    
    answer -= 1
    
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))