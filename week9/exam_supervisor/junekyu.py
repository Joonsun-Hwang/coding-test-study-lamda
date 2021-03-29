#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb

def solution(N, test_classes, A, B):

    answer = 0
    for i in range(N):
        num_applicant = int(test_classes[i])
        if num_applicant <= 0:
            answer += 0
        else:
            answer += 1
            num_applicant -= A
            if num_applicant > 0:
                answer += (num_applicant // B)
                if num_applicant % B:
                    answer += 1
            
    return answer


def main():
    N = input()
    test_classes_ = input()
    test_classes = test_classes_.split(' ')
    A_B = input()
    A, B = A_B.split(' ')
    answer = solution(int(N), test_classes, int(A), int(B))
    print(answer)


if __name__ == "__main__":
    main()
