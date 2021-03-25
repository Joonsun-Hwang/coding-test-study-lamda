#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb


def solution(N, cards):
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i - j] + cards[j - 1])

    answer = dp[N]
    return answer


def main():
    N = int(input())
    cards = list(map(int, input().split(' ')))

    answer = solution(N, cards)
    print(answer)


if __name__ == "__main__":
    main()
