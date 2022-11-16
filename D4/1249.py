# BFS
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(N):
    visited = [[-1 for i in range(N)] for i in range (N)]
    q = deque([(0, 0)])
    visited[0][0] = jido[0][0]

    while q:
        # 현재 방문한 곳
        ex, ey = q.popleft()

        current = visited[ex][ey]
        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            # 범위 내인지 확인
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1 or current +jido[nx][ny] < visited[nx][ny]: 
                    # 이전에 방문 + 새롭게 방문하는 곳이 현재 기록된 값보다 최소라면
                        visited[nx][ny] = current + jido[nx][ny]
                        q.append((nx, ny))

    return visited[N-1][N-1]


T = int(input())
for test_case in range(T):
    N = int(input())
    jido = []

    for i in range (N):
        jido.append(list(map(int, input().rstrip())))

    

    print("#{0} {1}".format(test_case+1, bfs(N)))
