from itertools import chain

def check(x,y,i):
    if i % 3 == 0:
        x+=1
        return x,y
    if i%3 ==1:
        y+=1
        return x,y
    if i%3 == 2:
        x-=1
        y-=1
        return x,y

def solution(n):
    snail=[[0]*i for i in range(1,n+1)]
    
    val = 1
    x, y = -1, 0
    for i in range(n):
        for j in range(i,n):
            x,y=check(x,y,i)
            snail[x][y]=val
            val+=1
    return list(chain(*snail))