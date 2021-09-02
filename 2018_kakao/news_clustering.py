def solution(str1, str2):
    answer = 0

    split_data1 = list(str1.lower())
    split_data2 = list(str2.lower())

    data1 = []
    data2 = []
    
    for i in range(len(split_data1)):
        if i == len(split_data1) - 1:
            break
        if (split_data1[i] + split_data1[i+1]).isalpha() == True: # isalnum()
            data1.append(split_data1[i] + split_data1[i+1])
        
    for i in range(len(split_data2)):
        if i == len(split_data2) - 1:
            break
        if (split_data2[i] + split_data2[i+1]).isalpha() == True:
            data2.append(split_data2[i] + split_data2[i+1])

    combined = 0

    for i in data1:
        if i in data2:
            data2.remove(i)
            combined += 1
    
    intersection = len(data1) + len(data2)

    if intersection == 0:
        return 65536
    else:
        answer = (combined / intersection) * 65536
        
    return int(answer)

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))