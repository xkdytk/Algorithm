def solution(people, limit):
    answer = 0

    people.sort(reverse = True)

    first = 0
    last = len(people) - 1

    while first <= last:

        if people[first] + people[last] > limit or first == last:
            first += 1
            answer += 1
        else:
            first += 1
            last -= 1
            answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))