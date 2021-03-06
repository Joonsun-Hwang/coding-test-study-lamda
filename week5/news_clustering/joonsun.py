from collections import Counter


def str2list(string):
    l = []

    for i in range(len(string) - 1):
        s = string[i] + string[i + 1]
        if s.isalpha():
            l.append(s.lower())

    return l


def jaccard_similarity(l1, l2):
    if not l1 and not l2:
        return 1

    n_inter = len(list((Counter(l1) & Counter(l2)).elements()))
    print(l1, Counter(l1), Counter(l1) & Counter(l2))
    print(list((Counter(l1) & Counter(l2)).elements()))
    n_union = len(l1) + len(l2) - n_inter
    return n_inter / n_union


def solution(str1, str2):
    str1_l = str2list(str1)
    str2_l = str2list(str2)
    return int(jaccard_similarity(str1_l, str2_l) * 65536)
