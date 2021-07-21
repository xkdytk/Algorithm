def solution(numbers):
    answer = ''

    if numbers.count(0) == len(numbers):
        return '0'
    
    else:
        num = list(map(str, numbers))
        num.sort(key=lambda x : x*3, reverse=True)
    
        answer = "".join(num)

        return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))