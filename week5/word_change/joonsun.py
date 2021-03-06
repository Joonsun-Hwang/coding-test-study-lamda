from collections import deque, Counter


def len_duplicated(str1, str2):
    counter = 0
    for s1, s2 in zip(str1, str2):
        if s1 == s2:
            counter += 1
    return counter


def bfs(graph, start, target):
    answer = []
    visited = [0] * len(graph)
    len_word = len(graph[0])
    queue = list([start])
    visited[start[0]] = 1

    while queue:
        current_node = queue.pop()
        idx = current_node[0]
        height = current_node[1]

        for i, node in enumerate(graph):
            if not visited[i] and len_word - 1 == len_duplicated(graph[idx], node):
                queue += [[i, height + 1]]
                visited[i] = 1
                print(queue)
                if node == target:
                    answer.append(height + 1)
                    print(answer)
    if not answer:
        return 0
    else:
        return min(answer)


def solution(begin, target, words):
    answer = []
    if target not in words:
        return 0

    root_list = []
    len_word = len(begin)
    for idx, word in enumerate(words):
        if len_word - 1 == len_duplicated(word, begin):
            root_list += [idx]
    for root in root_list:
        answer.append(bfs(words, [root, 1], target))
    return min(answer)
