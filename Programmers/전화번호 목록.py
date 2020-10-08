'''
https://programmers.co.kr/learn/courses/30/lessons/42577
1차 100/100

개선:
앞뒤로 완전 탐색 말고, sort()로 미리 정렬해놓고 앞에서 뒤로 한번만 검사
O(N**2) => O(NlogN)
zip()함수를 이용하여 2개의 객체 비교를 통합 => 근데 이건 뭐... 알아만 두자
'''

def solution(phone_book):
    phone_book.sort()
    for _ in range(len(phone_book)):
        compare = phone_book[0]
        phone_book = phone_book[1:]
        for phone in phone_book:
            if phone.startswith(compare):
                return False
    return True
