#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb

def solution(s):

    s = s[2:-2]
    s_list = s.split('},{')

    tup_list = []
    for s_ in s_list:
        tup_list.append(s_.split(','))
    tup_list.sort(key=lambda x: len(x))

    answer = []
    item = None
    for tup in tup_list:
        if len(tup) == 1:
            item = tup[0]
            answer.append(int(item))
        else:
            for a in answer:
                tup.remove(str(a))
            item = tup[0]
            answer.append(int(item))

    return answer


def main():
    #  input_str = input('Enter your string: ')

    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    answer = solution(s)
    print(answer)
    # [2, 1, 3, 4]

    s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
    answer = solution(s)
    print(answer)
    # [2, 1, 3, 4]

    s = "{{20,111},{111}}"
    answer = solution(s)
    print(answer)
    # [111, 20]

    s = "{{123}}"
    answer = solution(s)
    print(answer)
    # [123]

    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    answer = solution(s)
    print(answer)
    # [3, 2, 4, 1]



if __name__ == "__main__":
    main()
