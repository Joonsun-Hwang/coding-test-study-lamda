import sys
from defaultdict import deque
from copy import deepcopy

"""
BFS
Floyd-warshall?

"""

def BFS(i,j,count,visited):
    q=deque()
    if


def main():
    visited = deepcopy(riddle)
    for i in range(height):
        for j in range(width):
            if riddle[i][j] == "W":
                pass
            else:
                BFS(i,j,0,visited)


if __name__ == "__main__":
    input = sys.stdin.readline
    height, width = list(map(int,input().strip("\n").split()))
    riddle = []
    for _ in range(height):
        riddle.append(input().strip("\n").split())
    main()
    visited = None
