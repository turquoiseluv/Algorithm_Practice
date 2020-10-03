n = 5
fear = [2, 3, 1, 2, 2]

def solution(n, fear):
    answer = 0
    fear.sort(reverse=True)
    print(fear)

    ptr = 0
    while ptr < len(fear):
    	ptr += fear[ptr]
    	answer += 1
    return answer
    
print(solution(n, fear))

'''
근데 이거 생각해보니, 문제를 풀 수는 있고 방향성을 받을 수는 있어도,
해답 코드가 다를 경우, 이게 맞는건지 여러 입력을 확인해볼 수도 없고, 시간복잡도가 괜찮은건지 알 수가 없네 ㅡㅡ
그럼 이 책은 읽고 외우기만 하고, 온라인 저지가 있는 프로그래머스나 백준에서 1일 1문제 해야될 듯;;
'''