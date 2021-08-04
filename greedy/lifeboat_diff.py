from math import ceil

def solution(people, limit):
    answer = 0

    people.sort(reverse = True)

    while people:

        first = 0
        last = len(people) - 1

        if people[first] <= limit/2:
            answer += ceil(len(people)/2)
            break

        if people[first] + people[last] > limit or first == last:
            people.pop(first)
            answer += 1
        else:
            people.pop(last)
            people.pop(first)
            answer += 1

    return answer

# pop하는 과정이 생각보다 시간을 많이 사용한다. 정답과 과정은 같지만 시간이 훨씬 많이 걸렸다.

# 반복하다가, 맨 앞의 사람이 보트 제한 무게의 절반 이하가 되면, 무조건 맨 뒤의 사람과 같이 보낼 수 있으므로 남은 사람은 남은 사람 수의 절반의 보트만 있으면 된다.
# 위의 최적화 알고리즘을 사용했는데도 최적화를 하지 않은 pop을 사용하지 않은 코드가 속도가 더 빨랐다.

# pop이 오래 걸리는 이유는 pop(0) 의 경우 데이터를 지우고 한칸씩 앞으로 당기기 때문에 O(1)이 아니라 O(n)이 되기 때문이다.