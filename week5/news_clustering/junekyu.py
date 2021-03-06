#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb

alphas = [chr(i).lower() for i in range(65, 91)]


def make_set(string):

    multi_set = []
    for i in range(len(string) - 1):
        if string[i] in alphas and string[i + 1] in alphas:
            token = string[i] + string[i + 1]
            multi_set.append(token)

    return multi_set


def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()

    str1_mset = make_set(str1)
    str2_mset = make_set(str2)

    count = 0
    temp_str2_mset = str2_mset[:]
    for s1 in str1_mset:
        if s1 in temp_str2_mset:
            temp_str2_mset.remove(s1)
            count += 1
    intersection = count
    union = len(temp_str2_mset) + len(str1_mset)

    if union != 0:
        answer = intersection / union
    else:
        answer = 1
    answer = 65536 * answer

    return int(answer)


def main():
    #  input_str = input('Enter your string: ')

    str1 = "FRANCE"
    str2 = "french"
    answer = solution(str1, str2)
    print(answer)
    #  16384

    str1 = "handshake"
    str2 = "shake hands"
    answer = solution(str1, str2)
    print(answer)
    #  65536

    str1 = "aa1+aa2"
    str2 = "AAAA12"
    answer = solution(str1, str2)
    print(answer)
    #  43690

    str1 = "E=M*C^2"
    str2 = "e=m*^2"
    answer = solution(str1, str2)
    print(answer)
    #  65536


if __name__ == "__main__":
    main()
