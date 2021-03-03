#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pdb
import math

def solution(n, stations, w):
    answer = 0

    not_covered = []

    if stations[0]-w-1 > 0:
        not_covered.append(stations[0]-w-1)
    for i in range(len(stations)-1):
        if stations[i] + w < stations[i+1] - w - 1:
            not_covered.append(stations[i+1]-2*w-1-stations[i])
    if stations[-1]+w < n:
        not_covered.append(n-stations[-1]-w)

    cover_len = w*2+1
    for part in not_covered:
        answer += math.ceil(part/cover_len)

    return answer


def main():

    N = 11
    stations = [4, 11]
    W = 1
    answer = solution(N, stations, W)
    print(answer)
    # 3

    N = 16
    stations = [9]
    W = 2
    answer = solution(N, stations, W)
    print(answer)
    # 3



if __name__ == "__main__":
    main()
