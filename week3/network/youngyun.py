<<<<<<< HEAD
=======
def solution(n, computers):
    visited = [0] * n
    answer =0

    def _dfs(start):
        stack = [start]
        while stack:
            c = stack.pop()
            if  visited[c] == 0: # 방문한 적이 없다면
                visited[c] = 1 #방문했다고 알려준다.
                for i in range(0, len(computers[0])):
                    if visited[i] == 0 and computers[c][i] == 1: #한번도 방문하지 않은 곳이 있었는데 그게 만약 내가 방금 방문한곳과 연결이 되어있다?
                        stack.append(i) #그럼 너도 연결된거 니까 append해준다




    for i in range(len(computers)):
        if visited[i] == 0:
            _dfs(i)
            answer += 1


    return answer
>>>>>>> 1f4052bc70eea66c1ace634ac4879be9f1827da5
