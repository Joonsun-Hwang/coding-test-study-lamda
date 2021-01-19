def solution(numbers, target):
    answer = 0
    
    results = [+numbers[0], -numbers[0]]
    for i in numbers[1:]:
        results = [x+i for x in results] + \
            [x-i for x in results]  # 덧셈과 뺄셈으로 나올 수 있는 두가지 경우의 리스트
    answer = results.count(target)
    
    return answer
