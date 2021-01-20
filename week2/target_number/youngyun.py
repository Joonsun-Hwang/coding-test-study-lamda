from itertools import product
def solution(numbers, target):
    li = [[x, -x] for x in numbers]
    li2 = list(map(sum,product(*li)))
    return li2.count(target)