numbers = [2, 1, 3, 4, 1]


def solution(numbers):
    added = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            added.append(numbers[i]+numbers[j])
    return sorted(list(set(added)))


print(solution(numbers))
