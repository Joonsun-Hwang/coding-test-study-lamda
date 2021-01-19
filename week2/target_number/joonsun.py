def solution(numbers, target):
    answer = 0
    
    results = [+numbers[0], -numbers[0]]
    for i in numbers[1:]:
        results = [x+i for x in results] + \
            [x-i for x in results]
    answer = results.count(target)
    
    return answer
