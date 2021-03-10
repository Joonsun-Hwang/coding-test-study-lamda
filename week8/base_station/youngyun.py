import math
def solution(n, stations, w):
    stations.sort()
    cover_list = []
    uncover_distances=[]
    for s in stations:
        left = s-w
        right = s+w
        cover_list.append([left,right])
    for idx in range(1,len(cover_list)):
        distance=(cover_list[idx][0] - cover_list[idx-1][1]) - 1
        uncover_distances.append(distance)
    uncover_distances.append(cover_list[0][0]-1)
    uncover_distances.append(n-cover_list[-1][1])
    total=0
    for i in uncover_distances:
        total+=math.ceil(i/(1+2*w))
    return total
        
    