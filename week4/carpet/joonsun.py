def solution(brown, yellow):
    
    n = brown+yellow
    
    candis = []
    for i in range(1, int(n**0.5)+1):
        candi = []
        if n%i == 0:
            candi.append(i)
            if i != n//i:
                candi.append(n//i)
                candis.append(candi)
            else:
                candi.append(i)
                candis.append(candi)
    print(candis)
    
    # yellow = (x-2) * (y-2)
    # brown = (x+y-2) * 2
    for x, y in reversed(candis):
        if yellow == (x-2)*(y-2) and brown == (x+y-2)*2:
            return [max(x, y), min(x, y)]
