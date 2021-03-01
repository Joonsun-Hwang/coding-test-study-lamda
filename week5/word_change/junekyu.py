#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb
from collections import deque

def check_one_char(w1, w2):
    if len(w1) == len(w2):
        count = 0
        for i, w in enumerate(w1):
            if w != w2[i]: count += 1
            if count > 1:
                return False
        return True
    else:
        return False


def solution(begin, target, words):

    if not target in words:
        return 0
    depth = 0
    q = deque()
    q.append((begin, 0))
    while q:
        node, depth = q.popleft()
        if node == target:
            return depth
        for word in words:
            if check_one_char(node, word):
                q.append((word, depth + 1))
    answer = 0
    return answer


def main():

    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    answer = solution(begin, target, words)
    print(answer)
    4

    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log"]
    answer = solution(begin, target, words)
    print(answer)
    # 0


if __name__ == "__main__":
    main()
