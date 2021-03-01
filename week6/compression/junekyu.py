#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb


def LZW(msg, vocab):

    answer = []
    w = msg[0]
    index = 0
    while w in vocab:
        if index == len(msg):
            return [vocab[w]]

        w = msg[: index + 1]
        index += 1
    vocab[w] = len(vocab) + 1
    answer.append(vocab[w[:-1]])
    msg = msg[index - 1 :]
    return answer + LZW(msg, vocab)


def solution(msg):
    vocab = dict()
    for i, c in enumerate(range(ord("A"), ord("Z") + 1)):
        c = chr(c)
        vocab[c] = i + 1
    answer = LZW(msg, vocab)
    return answer


def main():
    #  input_str = input('Enter your string: ')

    msg = "KAKAO"
    answer = solution(msg)
    print(answer)
    # [11, 1, 27, 15]

    msg = "TOBEORNOTTOBEORTOBEORNOT"
    answer = solution(msg)
    print(answer)
    # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]

    msg = "ABABABABABABABAB"
    answer = solution(msg)
    print(answer)
    # [1, 2, 27, 29, 28, 31, 30]


if __name__ == "__main__":
    main()
