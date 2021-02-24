# def solution(stones, k):  # timed out
#     return min([max(stones[idx:idx+k]) for idx in range(len(stones)-k+1)])

def check_possible(l, k, c):
    count = 1
    l = [e-c for e in l]
    
    for e in l:
        if e <= 0:
            count += 1
        else:
            count = 1
        
        if count > k:
            return False
    return True

def solution(stones, k):  # binary search
    m, n = 1, 200000000
    while m <= n:
        answer = (m+n)//2
        if check_possible(stones, k, answer):
            m = answer+1
        else:
            n = answer-1
    
    return m
    
