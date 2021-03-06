# fares => start,from,요금
# 다익스트라? => 플로이드 와샬
import pdb


def solution(n, s, a, b, fares):
    INF = float("inf")
    graph = [[INF] * n for _ in range(n)]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = INF

    for start, end, fare in fares:
        graph[start - 1][end - 1] = fare
        graph[end - 1][start - 1] = fare
    # k는 거쳐가는 노드
    for k in range(n):
        # j는 출발 노드
        for i in range(n):
            # i는 도착노드
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    answer = float("inf")
    for i in range(n):
        if answer > graph[s - 1][i] + graph[i][a - 1] + graph[i][b - 1]:
            answer = graph[s - 1][i] + graph[i][a - 1] + graph[i][b - 1]
    return answer
