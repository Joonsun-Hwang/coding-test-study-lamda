def solution(n):
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for j in range(i, n):
            
            # 1phase: Down
            if i % 3 == 0:
                x += 1
            
            # 2phase: Left
            elif i % 3 == 1:
                y += 1
            
            # 3phase: Up
            elif i % 3 == 2:
                x -= 1
                y -= 1
                
            res[x][y] = num
            num += 1
            
    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer
