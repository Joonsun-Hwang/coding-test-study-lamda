def possible(n, times, m):
    for time in times:
        n -= m // time
        if n <= 0:
            return True
    else:
        return False


def solution(n, times):
    l, r = 1, max(times) * n + 1

    while l <= r:
        m = (l + r) // 2

        if possible(n, times, m):
            r = m - 1
        else:
            l = m + 1
    return l
