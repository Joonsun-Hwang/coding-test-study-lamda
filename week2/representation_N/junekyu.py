import pdb


def solution(N, number):
    answer = -1
    candidates = []
    for i in range(7):
        if i == 0:
            candidates.append([N])
        else:
            target_list = []
            target_list.append(int(str(N) * (i + 1)))
            for j in range(i):
                for prev_1 in candidates[j]:
                    for prev_2 in candidates[i - j - 1]:
                        target_list.append(prev_1 + prev_2)
                        target_list.append(prev_1 - prev_2)
                        target_list.append(prev_1 * prev_2)
                        if prev_2 != 0:
                            target_list.append(prev_1 // prev_2)
            candidates.append(list(set(target_list)))

        if number in candidates[i]:
            answer = i + 1
            break
    return answer


def main():
    N = 5
    number = 12
    answer = solution(N, number)
    print(answer)
    # 4

    N = 2
    number = 11
    answer = solution(N, number)
    print(answer)
    # 3


if __name__ == "__main__":
    main()
