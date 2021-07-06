def solution(phone_book):
    dic = {}
    length = []

    answer = True
    for i in phone_book:
        dic[i] = len(i)
        if len(i) not in length:
            length.append(len(i))
    
    for i in phone_book:
        for num in length:
            if len(i) > num:
                if i[:num] in dic:
                    answer = False
                    break
        if answer == False:
            break
    
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))