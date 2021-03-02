def solution(n, times):
    # 1분 이상 걸리므로
    left = 1
    # 1,000,000,000 이상 걸리므로
    right = max(times) * n
    num = 0
    while left <= right:
        mid = (left + right) // 2
        for t in times:
            num += mid // t
        if num >= n:
            right = mid - 1
        else:
            left = mid + 1
        num = 0
    return left
