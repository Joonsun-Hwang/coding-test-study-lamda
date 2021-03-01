#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb

def solution(new_id):
    # 1.
    new_id = new_id.lower()
    # 2. 3.
    can_use_list = [chr(i) for i in range(ord('a'), ord('z')+1)]
    can_use_list.append('-')
    can_use_list.append('_')
    can_use_list.append('.')
    n_list = [str(i) for i in range(10)]
    can_use_list.extend(n_list)

    temp_new_id = ""
    continuity_flag = False
    for c in new_id:
        if c in can_use_list:
            if c == '.' and continuity_flag == False:
                continuity_flag = True
                temp_new_id += c
            elif c == '.' and continuity_flag:
                continue
            else:
                continuity_flag = False
                temp_new_id += c
    new_id = temp_new_id

    # 4.
    if new_id:
        if new_id[0] == '.' and new_id:
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 5.
    if len(new_id) == 0:
        new_id = 'a'

    # 6.
    new_id = new_id[:15]
    
    # 7.
    while len(new_id) <= 2:
        new_id += new_id[-1]

    # do 4. again
    if new_id:
        if new_id[0] == '.' and new_id:
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    answer = new_id
    return answer


def main():
    #  input_str = input('Enter your string: ')
    new_id = "...!@BaT#*..y.abcdefghijklm"
    answer = solution(new_id)
    print(answer)
    # "bat.y.abcdefghi"

    new_id = "z-+.^."
    answer = solution(new_id)
    print(answer)
    # "z--"

    new_id = "=.="
    answer = solution(new_id)
    print(answer)
    # "aaa"

    new_id = "123_.def"
    answer = solution(new_id)
    print(answer)
    # "123_.def"

    new_id = "abcdefghijklmn.p"
    answer = solution(new_id)
    print(answer)
    # "abcdefghijklmn"



if __name__ == "__main__":
    main()
