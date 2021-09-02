import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    print(gyo)
    print(hap)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

    # set과 count를 이용해서 해결
    # 교집합과 합집합를 간단히 구현하기 위해서 set을 사용
    # 그러나 중복된 요소들이 제거되기 때문에 str1, str2에서 교집합과 합집합의 요소 개수를 세어서 다중 집합 교집합과 합집합의 개수를 구한다.

print(solution("aa1+aa2", "AAAA12"))