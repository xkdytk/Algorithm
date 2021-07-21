import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    print(n)
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

print(solution([3, 30, 34, 5, 9]))
# functools.cmp_to_key(func) 함수는 sorted와 같은 정렬 함수의 key 매개변수에 함수(func)를 전달할 때 사용하는 함수

#1) 6을 기준을 10과 비교하게 되면 610(6+10) > 106(10+6)이므로 10보다 6의 우선순위가 높으므로 10보다 6이 먼저 출력된다.
#   (옵션이 없다면 10이 먼저 출력될 것이지만, reverse=True라는 옵션이 있기 때문에 내림차순 정렬이 되기 때문)
#2) 같은 방법으로 6을 기준으로 2와 비교하게 되면 62 > 26이므로 2보다 6이 먼저 출력된다.
#3) 10을 기준으로 2와 비교하게 된다면 210 > 102이므로 10보다 2가 먼저 출력한다.