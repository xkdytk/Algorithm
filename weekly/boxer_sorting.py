from collections import defaultdict

def solution(weights, head2head):
    answer = []
    dic = defaultdict(list)

    for index, element in enumerate (head2head):
        win_num, match_num, winning_rate = 0, 0, 0
        for win_idx, result in enumerate(element):
            if result != "N":
                match_num += 1
            if result == "W": 
                winning_rate += 1
                if weights[win_idx] > weights[index]: 
                    win_num += 1
        if match_num != 0:
            winning_rate /= match_num
        else:
            winning_rate = 0
        dic[index].append(winning_rate)
        dic[index].append(win_num)
        dic[index].append(weights[index])

    dic = sorted(dic.items(), key=lambda x : (-x[1][0], -x[1][1], -x[1][2], x[0]))

    for i in dic:
        answer.append(i[0]+1)

    return answer

print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))
print(solution([145,92,86], ["NLW","WNL","LWN"]))
print(solution([60,70,60], ["NNN","NNN","NNN"]))