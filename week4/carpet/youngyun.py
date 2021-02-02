def solution(brown, yellow):
    answer =0 
    sum = brown+yellow
    li = []
    for i in range(3,brown-1): # 세로
        for j in range(3,brown-1): #가로
            if sum == i*j and j>=i :
                if (i-2) * (j-2) == yellow:
                    li.append([j,i])

    return li[-1]