def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

# int/int는 float이 되니 나누어떨어지더라도 나눈 결과의 타입을 int로 확실히 하기 위해서 사용
# 한줄로 깔끔하게 정리