from itertools import permutations

def solution(numbers):
    answer = 0
    
    # 문자열로 된 numbers를 한 문자씩 쪼갠 list로 바꿈
    numbers = list(numbers)
    
    # numbers를 조합해서 나올 수 있는 모든 경우의 문자열
    perm = list()
    for i in range(1, len(numbers)+1):  # 길이 1 부터 numbers까지
        perm += list(map(''.join, permutations(numbers, i)))
    perm = list(set(map(int, perm)))
    
    # 소수 찾기
    for num in comb:
        for mod in range(2, num+1):
            if num % mod == 0:
                if num == mod:
                    answer += 1
                else:
                    break
    
    return answer
