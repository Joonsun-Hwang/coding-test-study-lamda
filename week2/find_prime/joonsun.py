from itertools import permutations

def solution(numbers):
    answer = 0
    
    numbers = list(numbers)
    
    comb = list()
    for i in range(1, len(numbers)+1):
        comb += list(map(''.join, permutations(numbers, i)))
    comb = list(set(map(int, comb)))
    
    for num in comb:
        for mod in range(2, num+1):
            if num % mod == 0:
                if num == mod:
                    answer += 1
                else:
                    break
    
    return answer
