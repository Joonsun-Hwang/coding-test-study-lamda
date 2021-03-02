#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb


def solution(skill, skill_trees):
    
    answer = 0

    for skill_tree in skill_trees:
        flag = True
        skill_index = 0
        for skill_ in skill_tree:
            if skill_ in skill:
                if skill_ == skill[skill_index]:
                    skill_index += 1
                    if skill_index == len(skill):
                        skill_index -= 1
                else:
                    flag = False
        if flag:
            answer += 1
    return answer


def main():

    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

    answer = solution(skill, skill_trees)
    print(answer)
    # 2


if __name__ == "__main__":
    main()
