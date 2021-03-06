import math


def solution(n, stations, w):
    answer = 0
    lengths = []
    window = 2 * w + 1
    l = 1

    for station in stations:
        if station - w - 1 >= l:
            lengths.append(station - w - 1 - l + 1)
        l = station + w + 1

    if l <= n:
        lengths.append(n - l + 1)

    for length in lengths:
        answer += math.ceil(length / window)

    return answer
