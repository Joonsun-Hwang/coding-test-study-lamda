import heapq


def solution(jobs):
    count, last_t = 0, -1
    answer = 0
    wait_t = []
    jobs.sort()
    current_t = jobs[0][0]  # 첫 시작 시간
    while count < len(jobs):
        for start_t, taken_t in jobs:
            if last_t < start_t <= current_t:
                heapq.heappush(wait_t, (start_t, taken_t))
        if len(wait_t) > 0:
            count += 1
            last_t = current_t
            start_t, taken_t = heapq.heappop(wait_t)
            current_t += taken_t
            answer += current_t - start_t
        else:
            current_t += 1

    return answer // len(jobs)
