'''
실력체크 그냥 기출 랜덤이라 이렇게 정리하면 안되네 하.. ㅡㅡ
점수 70/100 추후 풀이 정리
'''

import re
import copy


def calculate(num1, num2, exp):
    if exp == "+":
        return num1 + num2
    if exp == "-":
        return num1 - num2
    if exp == "*":
        return num1 * num2


def getResults(eq, exp):
    eq.reverse()
    for i in range(3):
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
