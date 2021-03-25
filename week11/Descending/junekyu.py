#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb


def solution():

    N = int(input())
    max_values = []
    min_values = []
    for level in range(N):
        cur_in = list(map(int, input().split(' ')))
        if level == 0:
            max_values = cur_in[:]
            min_values = cur_in[:]
            continue
        else:
            left = max([max_values[0], max_values[1]]) + cur_in[0]
            mid = max([max_values[0], max_values[1], max_values[2]
                       ]) + cur_in[1]
            right = max([max_values[1], max_values[2]]) + cur_in[2]
            max_values[0] = left
            max_values[1] = mid
            max_values[2] = right

            left = min([min_values[0], min_values[1]]) + cur_in[0]
            mid = min([min_values[0], min_values[1], min_values[2]
                       ]) + cur_in[1]
            right = min([min_values[1], min_values[2]]) + cur_in[2]
            min_values[0] = left
            min_values[1] = mid
            min_values[2] = right

    print(str(max(max_values)) + " " + str(min(min_values)))


def main():

    solution()


if __name__ == "__main__":
    main()
