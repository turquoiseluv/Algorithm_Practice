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
