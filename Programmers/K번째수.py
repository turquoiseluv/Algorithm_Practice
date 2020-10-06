'''
https://programmers.co.kr/learn/courses/30/lessons/42748
1차 100/100

개선:
lambda로 answer 선언, for문, answer 반환 모두 통합
return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for c in commands:
    	answer.append(sorted(array[c[0]-1:c[1]])[c[2]-1])
    return answer

print(solution(array, commands))
