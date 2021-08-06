def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30001
    print(routes)

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer

# 이 코드는 내 코드의 30001로 지정해주는 부분 없이 그냥 카메라로 관측되는 곳이면 지나가게 설정