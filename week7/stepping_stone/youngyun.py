"""
꿀팀 = > 선형자료의 탐색 시간을 줄이는 법은 해시, 이분 탐색이다.
풀이 => 이분 탐색
1. 가장 맥시멈 값인 200000000을 놓는다
2. 절반씩 줄여나간다 left + right // 2
3. mid로 모든 돌다리 다 빼준다
4. 여기서 0또는 0보다 작은 돌다리의 개수를 구한다
5. 더한 개수가 k보다 크면 right를 mid+1로 , 만약 더 크면 left를 mid-1로 바꾼다

"""
import copy


def solution(stones, k):
    inf = 200000000

    left, right = 1, inf
    while left <= right:
        lot = 0
        mid = (left + right) // 2
        tmp = copy.deepcopy(stones)
        check = False
        for i in range(len(tmp)):
            tmp[i] -= mid
        for t in tmp:
            if t <= 0:
                lot += 1
            else:
                lot = 0
            if lot >= k:
                check = True
                break
        if check:
            right = mid - 1
        else:
            left = mid + 1

    return left
