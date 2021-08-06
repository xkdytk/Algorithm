def solution(price, money, count):
    answer = -1
    amount = int(count * (price + price*count) / 2)

    if money < amount:
        answer = amount - money
    
    else:
        answer = 0

    return answer

print(solution(3, 20, 4))