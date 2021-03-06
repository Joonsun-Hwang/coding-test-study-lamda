#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb
import copy


def solution(phone_book):
    flag = True
    for p in phone_book:
        temp_phone_book = list(phone_book)
        temp_phone_book.remove(p)
        for q in temp_phone_book:
            if q.split(p)[0] == "":
                return False
    return True


def main():
    inputs = ["119", "97674223", "1195524421"]
    answer = solution(inputs)
    print(answer)
    inputs = ["123", "456", "789"]
    answer = solution(inputs)
    print(answer)
    inputs = ["12", "123", "1235", "567", "88"]
    answer = solution(inputs)
    print(answer)


if __name__ == "__main__":
    main()
