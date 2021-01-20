import pdb
def solution(N, number):
    answer = -1
    pdb.set_trace()    
    if N == number:
        return 1
   
    s = [set() for x in range(8)]  # 4번 제한사항(최솟값이 8보다 크면 -1을 return 합니다.)
    for i, x in enumerate(s):
        x.add(int(str(N)*(i+1)))  # 개수 조합
    
    for i in range(1, len(s)):  # i는 몇개의 N을 썼는지에 대한 변수, 정확히는 i == n(N)-1
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:  # j + (i-j-1)은 i-1, 즉 N을 i-1번 사용한 결과는 i번째 인덱스에 저장됨
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2 != 0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i+1;
            break
    
    return answer

solution(5, 12)