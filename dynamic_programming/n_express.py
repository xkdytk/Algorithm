def solution(N, number):
    answer = -1
    prior = []
    for i in range(1, 9):
        case = set()
        case.add(int(str(N) * i))

        for j in range(0, i-1):
            for cal_1 in prior[j]:
                for cal_2 in prior[-j-1]:
                    case.add(cal_1 + cal_2)
                    case.add(cal_1 * cal_2)
                    case.add(cal_1 - cal_2)
                    if cal_2 != 0:
                        case.add(cal_1 // cal_2)

        if number in case:
            return i

        prior.append(case)

    return answer

print(solution(5, 12))
print(solution(2, 11))