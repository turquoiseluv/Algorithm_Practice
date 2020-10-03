x = 12


def solution(x):
    total = sum(list(map(int, list(str(x)))))
    if x % total == 0:
        return True
    return False


solution(x)
