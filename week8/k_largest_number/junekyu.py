#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pdb

def solution(array, commands):

    answer = []
    for command in commands:
        new_arr = array.copy()
        new_arr = new_arr[command[0]-1:command[1]]
        new_arr.sort()
        answer.append(new_arr[command[2]-1])

    
    return answer


def main():

    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    answer = solution(array, commands)
    print(answer)
    # [5, 6, 3]


if __name__ == "__main__":
    main()
