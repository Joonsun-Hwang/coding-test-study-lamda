# 지나치게 코드가 길며 시간복잡도도 상당히 좋지 않음 글자를 하나하나 맞춰보는 경우 O(n^3)인 경우도 생성됨 

def solution(words, queries):
    answer = []
    print(words)
    for query in queries :
        match = 0
        for word in words :
            flag = True
            j = 0
            i = 0
            if len(word) != len(query): # 애초에 길이가 다르면 비교 가치 없음
                continue
            else :
                if query[0] == '?': #처음엔 ?
                    while query[i] == '?': #언제까지 ? 인가?
                        i += 1
                    for idx in range(i, len(query)):
                        if query[idx] != word[idx]:
                            flag = False
                    
                    if flag == True:
                        match += 1
                    
                else : # 처음엔 문자
                    while query[i] != '?' :
                        i += 1
                    
                    while word[j] == query[j]:
                        j += 1
                    
                    if i == j :
                        match += 1
                    
                        
        answer.append(match)        
                     
    
    return answer