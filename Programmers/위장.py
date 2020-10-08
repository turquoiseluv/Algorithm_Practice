'''
https://programmers.co.kr/learn/courses/30/lessons/42578
1차 100/100

개선:
lambda로 answer 선언, for문, answer 반환 모두 통합
return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''
def solution(clothes):
    ans = 1
    dict = {}
    for cloth in clothes:
        if cloth[1] in list(dict.keys()):
            dict[cloth[1]] += 1
        else:
            dict[cloth[1]] = 1
    for val in list(dict.values()):
        ans *= val+1
    return ans-1