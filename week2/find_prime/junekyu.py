from itertools import permutations

def solution(numbers):
    answer = 0

    perms = set()
    for i in range(len(numbers)):
        permutation = permutations(numbers, i+1)
        for perm in permutation:
            num = int(''.join(perm))
            perms.add(num)

    for perm in perms:
        if is_prime(perm) == True:
            answer += 1

    return answer
       

def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        return True


def main():
    input_str= input('Enter your string: ')

    answer = solution(input_str)
    print(answer)


if __name__ == "__main__":
    main()
