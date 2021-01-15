#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb

def solution(prices):
    
    answer = []
    for i, p in enumerate(prices):
        count = 0
        for j in range(i + 1, len(prices)):
            count += 1
            if prices[j] < p:
                break
        answer.append(count)
                
    return answer

def main():
    #  input_str = input('Enter your string: ')
    input_list = [1, 2, 3, 2, 3]

    answer = solution(input_list)
    print(answer)
    # [4, 3, 1, 1, 0]

if __name__ == "__main__":
    main()
