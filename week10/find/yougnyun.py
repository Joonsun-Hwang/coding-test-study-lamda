import sys

"""
T는 비교 문자열 T의 길이는 n
P는 Pattern  P의 길이는 m
"""


def main():
    T_str = input().strip("\n")
    pattern = input().strip("\n")
    len_p = len(pattern)
    n_appear = 0
    idx_appear = []
    for idx in range(len(T_str)):
        if hash(T_str[idx : idx + len_p]) == hash(pattern):
            n_appear += 1
            idx_appear.append(idx + 1)

    print(n_appear)
    for answer in idx_appear:
        print(answer, end=" ")


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
