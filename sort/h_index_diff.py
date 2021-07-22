def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    print(list(enumerate(citations, start=1)))
    print(list(map(min,enumerate(citations, start=1))))
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

# sort로 정렬해서 가장 큰값부터 작은값으로 정렬한후, enumerate로 (index, value)형태로 묶는다. 
# (이렇게 묶으면 자동으로 각 논문이 인용된 수보다 같거나 많이 인용된 논문의 수를 알 수 있게 된다.), ex) (2,5) --> 5번 이상 인용된 논문이 2편
# (2, 5)는 둘 다 h 값으로 볼 수 있는데 h번 이상 인용된 논문이 h편 이상이므로 두 h가 큰 값으로 될 수 없으니 작은 값으로 해야한다.
# 그리고 최댓값(start = 1)부터 각 value에 대해 최솟값 value의 값을 min으로 추출하고, 이 추출된 값은 enumerate가 끝나는 citations 리스트의 크기에 해당하는 갯수가 나온다.
# 이들을 map으로 묶으면, 한 value의 입장에서 보는 최솟값 value의 집합이 나온다. 
# 즉 h값들의 집합이나온다. h값중 최대값을 max로 뽑아서 출력하면 된다.

print(solution([3, 0, 6, 1, 5]))
print(solution([0, 0, 0, 0, 1]))
print(solution([6, 5, 4, 1, 0]))