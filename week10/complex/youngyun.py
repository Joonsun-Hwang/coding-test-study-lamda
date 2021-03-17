import sys
import pdb


def main():
    num = int(input())
    complex = []
    live = 0
    many = 0
    answer = []
    for _ in range(num):
        complex.append(list(map(int,input().strip("\n"))))
    def _dfs(i, j):
        
        if i >= len(complex) or j >= len(complex) or i < 0 or j<0:
            return 
        if complex[i][j] == 0:
            return
        else:
            complex[i][j]=0
            nonlocal live
            live += 1
            _dfs(i,j+1)#우
            _dfs(i,j-1)#좌
            _dfs(i+1,j)#상
            _dfs(i-1,j)#하
    
    
    for i in range(len(complex)):
        for j in range(len(complex[0])):
            if complex[i][j] == 1:
                _dfs(i,j)
                answer.append(live)
                many += 1
                live = 0

    print(many)
    answer.sort()
    for ans in answer:
        print(ans)




if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    input = sys.stdin.readline
    main()