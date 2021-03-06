#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pdb


def dfs(computers, start_node):
    visited = []
    stack = []

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            #  connected nodes
            for i, edge in enumerate(computers[node]):
                if i == node:
                    continue
                if edge:
                    stack.append(i)
    return visited


def solution(n, computers):

    searched = []
    for start_node in range(n):
        visited = dfs(computers, start_node)
        print(visited)
        searched.append(visited)

    paths = set()
    for connection in searched:
        connection.sort()
        paths.add(str(connection))
    return len(paths)


def main():
    #  input_str = input('Enter your string: ')

    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    answer = solution(n, computers)
    print(answer)
    # 2

    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    answer = solution(n, computers)
    print(answer)
    # 1


if __name__ == "__main__":
    main()
