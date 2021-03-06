import string


def solution(msg):
    vocab = {alpha: i for i, alpha in enumerate(string.ascii_uppercase, start=1)}
    answer = []

    while msg:
        idx = 2
        while idx < len(msg):
            if msg[:idx] not in vocab:
                break
            idx += 1

        if idx == len(msg) and msg[:idx] in vocab:  # 마지막 글자일 경우의 처리
            answer.append(vocab[msg[:idx]])
            msg = ""
        else:
            answer.append(vocab[msg[: idx - 1]])
            vocab[msg[:idx]] = len(vocab) + 1
            msg = msg[idx - 1 :]

    return answer
