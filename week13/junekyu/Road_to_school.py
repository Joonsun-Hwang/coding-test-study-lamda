from collections import deque


def solution(m, n, puddles):

    mat = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [i, j] in puddles:
                continue
            elif i == 1 and j == 1:
                mat[i][j] = 1
            else:
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]

    return mat[n][m] % 1000000007


def main():

    m = 4
    n = 3
    puddles = [[2, 2]]
    answer = solution(m, n, puddles)
    print(answer)
    #  4

    m = 4
    n = 3
    puddles = [[2, 2], [2, 3]]
    answer = solution(m, n, puddles)
    print(answer)
    #  2

    m = 5
    n = 3
    puddles = [[2, 2], [2, 4]]
    answer = solution(m, n, puddles)
    print(answer)
    #  3


if __name__ == "__main__":
    main()

