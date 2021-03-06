def is_correct(string):
    stack = 0
    for sg in string:
        if sg == "(":
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                return False
    return True


def divide(string):
    right, left = 0, 0
    for idx, sg in enumerate(string):
        if sg == "(":
            left += 1
        else:  # sg == ')'
            right += 1
        if left == right:
            u = string[: left + right]
            v = string[left + right :]
            return u, v


def solution(p):
    empty = ""
    if p == "":  # 1단계
        return p
    u, v = divide(p)  # 2단계

    if is_correct(u):  # 3단계
        return u + solution(v)  # 3-1
    else:  # 4단계
        empty += "("
        empty += solution(v)
        empty += ")"
        u = u[1:-1]
        for sg in u:
            if sg == "(":
                empty += ")"
            else:
                empty += "("
        return empty
