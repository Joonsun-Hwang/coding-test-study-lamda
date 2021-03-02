def solution(array, commands):
    return [sorted(array[start-1:end])[order-1] for start, end, order in commands]