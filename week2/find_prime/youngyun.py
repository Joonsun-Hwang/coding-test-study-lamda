pfrom itertools import permutations
def solution(numbers):
    str_list=[]
    a = []
    
    size = len(numbers) + 1
    answer_set = set()
    answer = 0
    for i in numbers:
        str_list.append(i)
    for i in range(1,size):
        a.extend(list(map("".join,list(permutations(str_list,i)))))
    ans=set(map(int,a))
    for i in ans:
        num=is_prime(i)
        answer += num
    return answer

def is_prime(num):
    
    not_prime=[0,1]
    if num in not_prime:
        return 0
    for i in range(2,num):
        if num%i ==0 :
            return 0
    return 1
    
    
    
    