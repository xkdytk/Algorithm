def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
# 문자열을 정렬한 후 startswith를 사용하여 앞뒤문자열 모두 체크하도록 구현

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
# 문자열을 dictionary에 넣고, 한 글자씩 쪼갠 후 반복문을 돌며 하나씩 붙이면서 dictionary 내부에 해당 번호가 있는지 확인