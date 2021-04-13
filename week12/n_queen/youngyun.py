import pdb
answer = 0


def dfs(n, col, q):
    global answer
    if col == n:
        #         import pdb;pdb.set_trace()
        answer += 1
        return
    for i in range(n):
        q[col] = i
        for j in range(col):
            if q[col] == q[j] or abs(q[col]-q[j]) == col - j:
                break
        else:
            dfs(n, col+1, q)
    return answer


def solution(n):
    return dfs(n, 0, [-1]*n)
