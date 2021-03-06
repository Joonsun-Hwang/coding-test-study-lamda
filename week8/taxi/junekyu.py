#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb
from collections import deque


def solution(n, s, a, b, fares):

    s = s - 1
    a = a - 1
    b = b - 1

    mat = []
    for i in range(n):
        mat.append([0 for j in range(n)])

    for i in range(n):
        for j in range(n):
            if i == j:
                mat[i][j] = 0
            else:
                mat[i][j] = float("inf")

    for fare in fares:
        mat[fare[0] - 1][fare[1] - 1] = fare[2]
        mat[fare[1] - 1][fare[0] - 1] = fare[2]

    for k in range(n):  # passing node
        for i in range(n):  # start node
            for j in range(n):  # end node
                if mat[i][k] + mat[k][j] < mat[i][j]:
                    mat[i][j] = mat[i][k] + mat[k][j]

    answer = float("inf")
    for k in range(n):
        if mat[s][k] + mat[k][a] + mat[k][b] < answer:
            answer = mat[s][k] + mat[k][a] + mat[k][b]

    return answer


def main():

    n = 6
    s = 4
    a = 6
    b = 2
    fares = [
        [4, 1, 10],
        [3, 5, 24],
        [5, 6, 2],
        [3, 1, 41],
        [5, 1, 24],
        [4, 6, 50],
        [2, 4, 66],
        [2, 3, 22],
        [1, 6, 25],
    ]
    answer = solution(n, s, a, b, fares)
    print(answer)
    # 82

    n = 7
    s = 3
    a = 4
    b = 1
    fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    answer = solution(n, s, a, b, fares)
    print(answer)
    # 14

    n = 6
    s = 4
    a = 5
    b = 6
    fares = [
        [2, 6, 6],
        [6, 3, 7],
        [4, 6, 7],
        [6, 5, 11],
        [2, 5, 12],
        [5, 3, 20],
        [2, 4, 8],
        [4, 3, 9],
    ]
    answer = solution(n, s, a, b, fares)
    print(answer)
    # 18


if __name__ == "__main__":
    main()
