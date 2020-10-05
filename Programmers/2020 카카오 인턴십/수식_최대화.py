'''
실력체크 그냥 기출 랜덤이라 이렇게 정리하면 안되네 하.. ㅡㅡ
1차 점수 70/100 추후 풀이 정리

2차 100 / 100
이 문제도 디버깅을 해보니,
pop을 사용한 stack 구현이였기 때문에,
시간 복잡도 1인 list.pop()을 위하여 eq.reverse()로 거꾸로 수식을 계산해야 했는데
eq = save 하는데 반복문 안에 reverse를 안 넣고 시작할 때 한번만 한 문제였다.
70점은 어떻게 맞았지 ;;
'''

import re
import copy

expression = "50*6-3*2"

def calculate(num1, num2, exp):
    if exp == "+":
        return num1 + num2
    if exp == "-":
        return num1 - num2
    if exp == "*":
        return num1 * num2


def getResults(eq, exp):
    for i in range(3):
        eq.reverse()
        save = []
        while eq:
            x = eq.pop()
            if x == exp[i]:
                save.append(calculate(save.pop(), eq.pop(), x))
            else:
                save.append(x)
        eq = save
    return save[0]


def solution(expression):
    exp = ['+', '-', '*']
    eq = re.findall('[+-/*]|\d+', expression)
    for i in range(0, len(eq), 2):
        eq[i] = int(eq[i])
    x = []

    for i in range(3):
        for j in range(3):
            if exp[j] == exp[i]:
                continue
            for k in range(3):
                if exp[k] == exp[i] or exp[k] == exp[j]:
                    continue
                temp = copy.deepcopy(eq)
                x.append(getResults(temp, [exp[i], exp[j], exp[k]]))
    return sorted(list(map(abs, x)), reverse=True)[0]

print(solution(expression))