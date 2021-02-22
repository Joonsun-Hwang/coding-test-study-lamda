import re
def solution(s):
    s = eval(s[1:-1])
    s = list(s)
    if len(s) > 1:
        s.sort(key=lambda x : len(x))
    else :
        return list(s)
    answer = []
    for sg in s:
        for ssg in sg:
            if ssg not in answer:
                answer.append(ssg)
                
    return answer