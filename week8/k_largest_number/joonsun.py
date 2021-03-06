def solution(array, commands):
    answer = []
    for com in commands:
        cutted_array = array[com[0] - 1 : com[1]]
        cutted_array = sorted(cutted_array)
        answer += [cutted_array[com[2] - 1]]
    return answer
