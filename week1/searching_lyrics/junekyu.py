#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb

def solution(words, queries):
    answer = []
    for query in queries:
        count = 0
        if query.split('?')[0] == '':
            short_query = query.split('?')[-1]
            for word in words:
                if len(word) == len(query):
                    if word.split(short_query)[-1] == '':
                        count += 1
        else:
            short_query = query.split('?')[0]
            for word in words:
                if len(word) == len(query):
                    if word.split(short_query)[0] == '':
                        count += 1
        answer.append(count)
    return answer


def main():
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    answer = solution(words, queries)
    print(answer)
    # [3, 2, 4, 1, 0]

if __name__ == "__main__":
    main()
