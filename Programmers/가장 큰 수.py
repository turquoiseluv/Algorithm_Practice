'''
유사 풀이 참조
'''

from itertools import permutations

numbers = [0]

def solution(numbers):
	numbers = list(map(str, numbers))
	# 1000이하는 x*3 연결하여 비교하면 잘 비교 됨 / key=lambda를 사용해서 정리할 필요없이 깔끔 ;;
	numbers.sort(key = lambda x: x*3, reverse=True)
	# str(int())는 [0, 0, 0] => 000 방지
	return str(int("".join(numbers)))

print(solution(numbers))

'''
# 유사 풀이 2

import functools

# key=functools로 직접 정렬 공식 작성
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
'''
