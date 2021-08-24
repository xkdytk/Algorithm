def solution(table, languages, preference):
    answer = ''
    dict = {}

    for i in range(len(table)):
        tmp = table[i].split()
        for j in range(len(languages)):
            if languages[j] in tmp:
                index = tmp.index(languages[j])          
                if tmp[0] in dict:
                    dict[tmp[0]] = dict.get(tmp[0]) + (6-index) * preference[j]                 
                else:
                    dict[tmp[0]] = (6-index) * preference[j]

    answer = sorted(dict, key = lambda x : (-dict[x], x))[0]

    return answer

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))