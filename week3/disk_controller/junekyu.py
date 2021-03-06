#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq
from collections import deque
import pdb


def solution(jobs):

    num_of_works = len(jobs)
    jobs = deque(sorted(jobs))

    time_stamp = 0
    jobs_done = 0
    waiting_time = 0
    candidates = []

    while jobs_done < num_of_works:
        if not candidates:
            req_time, take_time = jobs.popleft()
            waiting_time += take_time
            time_stamp = req_time + take_time
        else:
            take_time, req_time = heapq.heappop(candidates)
            waiting_time += time_stamp - req_time + take_time
            time_stamp += take_time
        jobs_done += 1
        while jobs and jobs[0][0] <= time_stamp:
            heapq.heappush(candidates, jobs.popleft()[::-1])
    return waiting_time // num_of_works


def main():
    #  input_str = input('Enter your string: ')
    jobs = [[0, 3], [1, 9], [2, 6]]

    answer = solution(jobs)
    print(answer)
    # 9


if __name__ == "__main__":
    main()
