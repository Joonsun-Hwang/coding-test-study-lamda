# 시험장 갯수
n = int(input())
n_exams = list(map(int, input().split()))
main, support = list(map(int, input().split()))
answer = 0
for idx in range(len(n_exams)):
    n_exams[idx] -= main
    if n_exams[idx] <= 0:
        n_exams[idx] = 0
    answer += 1

    num = n_exams[idx] // support
    if n_exams[idx] % support != 0:
        num += 1
    answer += num

print(answer)
