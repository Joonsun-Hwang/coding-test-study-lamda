"""
BFS 알고리즘은 queue 와 while 을 사용하여 구현해야하고
DFS 알고리즘은 stack 또는 recursive를 사용하여 구현해야한다.
"""

from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())  # 세로, 가로 길이
board = [list(input().strip()) for _ in range(n)]  # strip은 공백을 제거 하는것

"""
4차원 배열을 선언함
왜냐하면 빨간 구슬, 파란구슬 2개가 동시에 움직이기 때문에
각 2개의 구슬 x,y 좌표를 visited 배열에 4차원으로 선언하고 False로 초기화
[빨간 구슬의 x좌표],[빨간 구슬의 y좌표],[파란 구슬의 x 좌표],[파란 구슬의 y좌표]
"""
visited = [[[[False] * m for _ in range(n)]
            for _ in range(m)] for _ in range(n)]


"""
구슬이 움직일 수 있는 x,y 좌표를 만들고, collection의 deque를 사용하여 queue를 생성
dx, dy는 밑에 코드에서 보면 알겠지만 pair 시킴
(-1,0)  왼쪽
(0,1)   위쪽  
(1,0)   오른쪽
(0,-1)  
"""
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -
                         1)  # 왼쪽 위쪽, 오른쪽,아래쪽(x,y)좌표를 의미함 => 밑에 코드에서 보면 알겠지만
q = deque()


def init():
    rx, ry, bx, by = [0] * 4  # 초기화 0,0,0,0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":  # board에 빨간 구슬이라면 좌표값 저장
                rx, ry = i, j
            elif board[i][j] == "B":
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))  # 위치 정보와 depth
    visited[rx][ry][bx][by] = True


def move(x, y, dx, dy):
    count = 0  # 이동한 칸수
    # 다음 이동이 벽이거나 구멍일 때까지
    while (
        board[x + dx][y + dy] != "#" and board[x][y] != "O"
    ):  # 1. 왼쪽, 2.  위쪽, 3. 오른쪽, 4. 아래쪽
        x += dx
        y += dy
        count += 1
    return x, y, count


def bfs():
    init()
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break
        for i in range(len(dx)):  # 4방향으로 시도
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i])  # RED
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i])  # BLUE

            if board[next_bx][next_by] == "O":
                continue
            if board[next_rx][next_ry] == "O":
                print(depth)
                return
            """
            여기서 왜 count를 move에서 return 해주는 지 알 수 있다.
            여기서 만약 빨간색 공이 파란색 공보다 x 방향으로 더 많이 갔다면
            즉 r_count > b_count 이면 빨간색이 뒤에 있었으니까 더 많이 간것이다
            y축도 일치한다 
            ex: r이 x가 10의 위치에 있고 b가 x의 9의 위치에 있고 x가 1인곳까지 간다고 할때
            r은 9만큼 움직여야 하지만 b는 8만큼 움직이면 된다.
            따라서 b|r 이렇게 있다
            """
            if next_rx == next_bx and next_ry == next_by:
                if r_count > b_count:
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]

            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth + 1))
    print(-1)


bfs()
