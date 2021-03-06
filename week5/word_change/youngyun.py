import collections


def solution(begin, target, words):
    def can_change(cur_word):
        candidate = []
        for word in words:
            check = [True for x, y in zip(word, cur_word) if x != y]
            if len(check) == 1:
                candidate.append(word)
        return candidate

    que = collections.deque([(begin, 0)])
    visited = set([begin])
    while que:
        cur_word, cur_time = que.popleft()

        if cur_word == target:
            return cur_time

        for can in can_change(cur_word):
            if can not in visited:
                visited.add(can)
                que.append([can, cur_time + 1])
    return 0
