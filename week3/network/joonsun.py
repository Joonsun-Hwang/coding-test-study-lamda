def dfs(computers, visited, start):
    stack = [start]
    while stack:
        j = stack.pop()
        if visited[j] == 0:
            visited[j] = 1
        for i in range(0, len(computers)):
            if computers[j][i] == 1 and visited[i] == 0:
                stack.append(i)


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    for i in range(len(visited)):  # 모두 방문할 때까지
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
    return answer
