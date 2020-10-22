def getNode(node):
	num = 1
	ans = []
	for n in node:
		ans += n[:num]
		num += 1
	return ans

def solution(n):
	node = []
	for _ in range(n):
		node.append([0]*n)

	curX = 0
	curY = -1

	start = 1
	turn = 0

	while turn<n:
		for _ in range(n-turn):
			if turn%3 == 0:
				curY += 1
			if turn%3 == 1:
				curX += 1
			if turn%3 == 2:
				curX -= 1
				curY -= 1
			node[curY][curX] = start
			start += 1
		turn += 1

	return getNode(node)


print(solution(6))