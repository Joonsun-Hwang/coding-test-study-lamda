"""
집합 A와 집합 B가 공집합일 경우에는 나눗셈이 정의되지 않아 J(A,B) = 1로 정의
"""
"""
1. 입력 모두를 소문자로 바꾼다.
2. 두 글짜씩으로 리스트를 만들어 준다.
3. isalpha 활용
4. for in 연산을 통해 얼마나 겹치있는 게 있나 확인한다.
5. 겹치는 것은 Counter &연산자 그리고 합집합은 | 연산자 사용
"""
import collections


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = []
    str2_list = []
    cross = 0

    for idx in range(len(str1) - 1):
        tmp = ""
        for i in range(idx, idx + 2):
            tmp += str1[i]
        if tmp.isalpha():
            str1_list.append(tmp)

    for idx in range(len(str2) - 1):
        tmp = ""
        for i in range(idx, idx + 2):
            tmp += str2[i]
        if tmp.isalpha():
            str2_list.append(tmp)

    c1 = collections.Counter(str1_list)
    c2 = collections.Counter(str2_list)
    cross = len(list((c1 & c2).elements()))
    union = len(list((c1 | c2).elements()))
    if union == 0:
        return 65536
    else:
        return int((cross / union) * 65536)
