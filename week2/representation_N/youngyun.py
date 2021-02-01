"""
N:표현할 수(5)
number : 표현당해야 하는 수 (12)
"""

def solution(N, number):
    if number == N:
        return 1
    answer = -1
    a = [set() for _ in range(8)]
    
    for idx, value in enumerate(a):
        value.add(int(str(N)*(idx+1)))
        
    for i in range(1, len(a)):
        for j in range(i):
            for k in a[j]:
                for l in a[i-j-1]:
                    a[i].add(k+l)
                    a[i].add(k-l)
                    a[i].add(k*l)
                    if l != 0 :
                        a[i].add(k/l)
                        
        if number in a[i]:
            answer = i+1
            break
        
    return answer        