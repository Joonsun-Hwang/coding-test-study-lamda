def solution(numbers, target):
    answer = []
    value = [0] * len(numbers)
    index = 0
    count = 0
    answer = recursive(value, numbers, index, target, count)

    return answer

def recursive(value, numbers, index, target, count):
    
    if index == len(numbers):
        if (value[-1] == target):
            return count + 1
        else:
            return count

    # plus
    if index == 0:
        value[index] = numbers[index]
    else:
        value[index] = value[index-1] + numbers[index]
    count = recursive(value, numbers, index+1, target, count)

    # minus
    if index == 0:
        value[index] = -numbers[index]
    else:
        value[index] = value[index-1] - numbers[index]

    count = recursive(value, numbers, index+1, target, count)

    return count

def main():
    numbers = [1, 1, 1, 1, 1]
    target = 3
    answer = solution(numbers, target)
    print(answer)
    # 3

if __name__ == "__main__":
    main()
