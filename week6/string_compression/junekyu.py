#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pdb


def compression(s, comp_len):

    index = 0
    compressed_str = ""
    while index < len(s):
        if s[index : index + comp_len] == s[index + comp_len : index + 2 * comp_len]:
            count = 1
            next_index = index + comp_len
            while next_index < len(s) - comp_len:
                if (
                    s[index : index + comp_len]
                    == s[
                        next_index
                        + count * comp_len : next_index
                        + (count + 1) * comp_len
                    ]
                ):
                    count += 1
                else:
                    break

            compressed_str += str(count + 1)
            compressed_str += s[index : index + comp_len]
            index += (count + 1) * comp_len
        else:
            compressed_str += s[index : index + comp_len]
            index += comp_len
            if index >= len(s) - comp_len:
                compressed_str += s[index:]
                break

    #  print(comp_len)
    #  print(compressed_str)
    return len(compressed_str)


def solution(s):
    min_len = len(s)

    for i in range(min_len // 2):

        #  pdb.set_trace()
        cur_len = compression(s, i + 1)
        if cur_len < min_len:
            min_len = cur_len

    #  pdb.set_trace()

    return min_len


def main():
    s = "xxxxxxxxxxyyy"
    answer = solution(s)
    print(answer)
    # 5

    s = "bbaabaaab"
    answer = solution(s)
    print(answer)
    # 8

    s = "zzzbbabbabba"
    answer = solution(s)
    print(answer)
    # 7

    s = "aabbaccc"
    answer = solution(s)
    print(answer)
    # 7

    s = "ababcdcdababcdcd"
    answer = solution(s)
    print(answer)
    # 9

    s = "abcabcdede"
    answer = solution(s)
    print(answer)
    # 8

    s = "abcabcabcabcdededededede"
    answer = solution(s)
    print(answer)
    # 14

    s = "xababcdcdababcdcd"
    answer = solution(s)
    print(answer)
    # 17


if __name__ == "__main__":
    main()
