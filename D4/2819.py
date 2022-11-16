# dfs
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, count, numString):
    numString += board[x][y]
    count += 1

    if count == 7:
        unique.add(numString)
        return

    for i in range (4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<4 and 0<=ny<4:
            dfs(nx, ny, count, numString)

T = int(input())
for test_case in range(T):
    board = []
    unique = set()
    numString = ''

    for i in range (4):
        board.append(list(map(str, input().split())))

    for i in range (4):
        for j in range (4):
            dfs(i, j, 0, numString)

    print("#{0} {1}".format(test_case+1, len(unique)))