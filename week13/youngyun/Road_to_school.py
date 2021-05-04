def solution(col, row, puddles):
    MAP = [[0] * col for _ in range(row)]
    MAP[0][0] = 1
    puddle = [[y - 1, x - 1] for x, y in puddles]
    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                continue
            else:
                if [i, j] in puddle:
                    MAP[i][j] == 0
                else:
                    MAP[i][j] = MAP[i - 1][j] + MAP[i][j - 1]
    return MAP[i][j] % 1000000007
