from collections import deque


def is_correct(string):  # 올바른 괄호인지 확인
    stack = []  # stack 사용
    for s in string:
        if s == "(":
            stack.append(s)
        elif stack:
            stack.pop()
    return not stack


def detatch(string):  # u, v로 분리
    queue = deque(string)
    open_p, close_p = 0, 0
    u, v = "", ""

    while queue:  # 큐사용
        u += queue.popleft()
        if u[-1] == "(":
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            break  # 균형 잡힌 괄호

    v = "".join(list(queue))
    return u, v


def reverse(u):  # 뒤집기
    return "".join([")" if s == "(" else "(" for s in u])


def recursive(string):
    if string == "":  # 1번
        return ""
    u, v = detatch(string)  # 2번
    if is_correct(u):  # 3번
        return u + recursive(v)
    else:  # 4번
        return "(" + recursive(v) + ")" + reverse(u[1:-1])


def solution(p):
    return p if is_correct(p) else recursive(p)
