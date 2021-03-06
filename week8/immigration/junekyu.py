#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb


def solution(n, times):

    answer = 0

    min_time = 1000000000
    for time in times:
        if time < min_time:
            min_time = time

    start = min_time
    end = n * min_time
    while start <= end:
        mid = (start + end) // 2

        checked = 0
        # check
        for time in times:
            checked += mid // time

        if checked >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


def main():

    n = 6
    times = [7, 10]
    answer = solution(n, times)
    print(answer)
    # 26


if __name__ == "__main__":
    main()
