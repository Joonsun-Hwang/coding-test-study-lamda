"""
문제 이해 
답은 문제가 물어본것은 각 작업의 요청부터 종료까지 걸린 시간의 평균
그니까 대기시간은 포함이 안되는것 
예시 
[[0, 2], [1, 15], [31, 2]] 가 입력이면
실제로 요청부터 종료까지 걸린 시간의 평균은 [2]+ [(2-1) + 15] +[2]  //3 이 된다. 
"""

def solution(jobs):
    answer = 0
    start = 0 # 여태까지 진행된 시간(대기시간 + 일한시간)
    jobs = sorted(jobs, key = lambda x : x[1])
    lj = len(jobs)
    while len(jobs)!=0:
        for i in range(len(jobs)):
            if start >= jobs[i][0]:
                start = start + jobs[i][1] #jobs[i][1]은 소요되는 작업 시간 그시간을 모두 다 더한게 start
                answer = answer - jobs[i][0] +start # jobs[i][0] - start 는 기다리는 시간은 삭제한것
                jobs.pop(i) # 사용했으니 삭제
                break
            
            if len(jobs)-1 == i: #작업한 시간을 모두다 더한값 작업을 다 해도 일이 안들어 온것
                start += 1
    
    answer = answer // lj
    return answer