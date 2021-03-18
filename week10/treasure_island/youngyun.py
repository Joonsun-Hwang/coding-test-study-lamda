import sys
from collections import deque


def main(i, j, cnt):

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque()
    q.append((i, j, cnt))
    c = [[0] * col for _ in range(row)]
    while q:
        i, j, cnt = q.popleft()
        c[i][j] = 1
        for derivate in range(4):  # 좌하우상
            if (
                i + dx[derivate] >= 0
                and j + dy[derivate] >= 0
                and i + dx[derivate] < row
                and j + dy[derivate] < col
                and riddle[i + dx[derivate]][j + dy[derivate]] == "L"
                and c[i + dx[derivate]][j + dy[derivate]] == 0
            ):
                c[i + dx[derivate]][j + dy[derivate]] = 1
                q.append(
                    (
                        i + dx[derivate],
                        j+ dy[derivate],
                        cnt + 1,
                    )
                )

    return cnt


if __name__ == "__main__":
    input = sys.stdin.readline
    row, col = map(int, input().strip("\n").split())
    riddle = []
    cnt = -1
    for _ in range(row):
        tmp = list(input().strip("\n"))
        riddle.append(tmp)
    for i in range(row):
        for j in range(col):
            if riddle[i][j] == "L":
                cnt = max(cnt, main(i, j, 0))
    print(cnt)
