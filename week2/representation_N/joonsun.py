def solution(N, number):
    answer = -1
    
    if N == number:
        return 1
    
    s = [set() for x in range(8)]  # 4번 제한사항
    for i, x in enumerate(s):
        x.add(int(str(N)*(i+1)))  # 개수 조합
    
    for i in range(1, len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2 != 0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i+1;
            break
    
    return answer
