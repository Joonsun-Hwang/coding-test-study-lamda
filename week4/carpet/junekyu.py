#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check_divisibility(n, m):
    if n % m == 0:
        return True
    else:
        return False

def len_boundary(i, j):
    return i*2 + j*2 + 4

def solution(brown, yellow):
    answer = []
    if yellow == 1:
        return [3, 3]
    for i in range(1, yellow):
        if check_divisibility(yellow, i):
            j = int(yellow / i)
            if j >= i:
                #  print('check brown')
                if brown == len_boundary(i, j):
                    return [j+2, i+2]

    return answer


def main():
    #  input_str = input('Enter your string: ')
    brown = 10
    yellow = 2
    answer = solution(brown, yellow)
    print(answer)
    #  [4, 3]

    brown = 8
    yellow = 1
    answer = solution(brown, yellow)
    print(answer)
    #  [3, 3]

    brown = 24
    yellow = 24
    answer = solution(brown, yellow)
    print(answer)
    #  [8, 6]



if __name__ == "__main__":
    main()
