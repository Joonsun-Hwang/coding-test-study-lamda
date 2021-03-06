#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb


def solution(stones, k):
    answer = 0
    minimum = 0
    maximum = max(stones)
    mid = (minimum + maximum) // 2

    while minimum <= maximum:

        temp_stones = [stone - mid for stone in stones]
        cur_crossed = maximum

        flag = True
        count = 0
        for step in range(len(temp_stones)):
            if temp_stones[step] <= 0:
                count += 1
                if count >= k:
                    flag = False
                    break
            else:
                count = 0

        if flag:
            minimum = mid + 1
            mid = (minimum + maximum) // 2
        else:
            answer = mid
            maximum = mid - 1
            mid = (minimum + maximum) // 2

    return answer


def main():

    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    answer = solution(stones, k)
    print(answer)
    # 3


if __name__ == "__main__":
    main()
