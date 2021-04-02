from collections import defaultdict, deque

h, w = map(int, input().split())
maze = []
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)
for _ in range(h):
    maze.append(list(input()))
visited = defaultdict(int)


def init(maze):
    rx=ry=bx=by=0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "R":
                rx = i
                ry = j
            if maze[i][j] == "B":
                bx = i
                by = j
    visited[(rx, ry, bx, by)] = 1
    # import pdb;pdb.set_trace()
    return rx, ry, bx, by


def move(sx, sy, dx, dy):
    count = 0
    while maze[sx + dx][sy + dy] != "#" and maze[sx + dx][sy + dy] != "O":
        sx += dx
        sy += dy
        count += 1
    return sx, sy, count


def dfs(rx, ry, bx, by, count):
    q = deque()
    q.append([rx, ry, bx, by, count])
    while q:

        rx, ry, bx, by, count = q.popleft()
        if count > 10:
            print(-1)
            return
        for i in range(4):
            next_rx, next_ry, rcount = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, bcount = move(bx, by, dx[i], dy[i])

            if maze[next_bx + dx[i]][next_by + dy[i]] == "O":
                continue
            if maze[next_rx + dx[i]][next_ry + dy[i]] == "O":
                print(count)
                return
            if next_rx==next_bx and next_ry==next_by:
                if rcount>bcount:
                    next_rx-=dx[i]
                    next_ry-=dy[i]
                else :
                    next_bx-=dx[i]
                    next_by-=dy[i]

            # import pdb;pdb.set_trace()
            if not visited[(next_rx, next_ry, next_bx, next_by)]:
                visited[(next_rx, next_ry, next_bx, next_by)] = 1
                q.append((next_rx, next_ry, next_bx, next_by,count+1))
    print(-1)


rx, ry, bx, by = init(maze)
dfs(rx, ry, bx, by, 1)
