'''
풀이 분석
1. permutations로 경우의 수 모두 구하기
2. \D로 숫자외의 기호를 기준으로 split (수식에 사용 굿)
3. eval = 문자열을 숫자로 계산 "3*5"(str) => 15(int)
4. reverse 정렬 후 i[0] 보다는 -> max()로 간단하게
'''

from itertools import permutations
import re
expression = "50*6-3+2"


def solution(expression):
    op = [x for x in ['*', '+', '-'] if x in expression]
    op = [list(y) for y in permutations(op)] # 1
    ex = re.split(r'(\D)', expression) # 2

    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex: # 3
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    return max(abs(int(x)) for x in a) # 4


print(solution(expression))
