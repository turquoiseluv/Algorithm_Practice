'''
1차 100 / 100
idx와 citations[idx] 비교하는 단순 풀이
'''

citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations.sort(reverse=True)
    for h in range(len(citations)):
        if h+1 > citations[h]:
            return h
    return len(citations)

'''
유사 풀이

def solution(citations):
    citations.sort(reverse=True)
    # 여기서 인덱스랑 값이랑 비교하는 개념은 비슷한데
    # enuerate해서 얻은 인덱스를 각 값과 비교해서 그걸 넘는 인덱스 값을
    # 최소값 구하는 방향으로 구한게 ;;
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

print(solution(citations))
'''