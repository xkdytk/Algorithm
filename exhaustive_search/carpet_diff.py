def solution(brown, red):
    x = (brown + 4 + ((brown + 4) ** 2 - 16 * (brown + red)) ** 0.5) / 4
    y = (brown + red) // x
    return [max(int(x), int(y)), min(int(x), int(y))]

# 가로의 길이를 x, 세로의 길이를 y라 한다.
# x*y = brown + red이며, (x-2)*(y-2) = red이다.
# 이 두 방정식을 풀면 2x^2 - (brown+4)x + 2red + 2brown = 0 이고
# 근의 공식에 의해 x = (brown + 4 + ((brown + 4) ** 2 - 16 * (brown + red)) ** 0.5) / 4, y = (brown + red) / x 이다.
# 둘 중 더 큰 값을 가로에, 더 작은 값을 세로에 넣어주면 된다.