def solution(name):
    answer = 0
    index = 0
    
    arr = list(name)
    count = [0] * len(arr)

    for i in range (len(arr)):
        if ord(arr[i]) - ord('A') > 13:
            count[i] = 26 - (ord(arr[i]) - ord('A'))
        else:
            count[i] = ord(arr[i]) - ord('A')

    while True:
        answer += count[index]
        count[index] = 0

        if count.count(0) == len(arr):
            break

        right, left = 1, 1

        while count[index+right] == 0:
            right += 1
        
        while count[index-left] == 0:
            left += 1
        
        if right > left:
            answer += left
            index -= left
        else:
            answer += right
            index += right
    
    return answer

print(solution("JEROEN"))
print(solution("JAN"))
print(solution("ABAAAAAAAAABB"))