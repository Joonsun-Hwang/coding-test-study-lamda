def solution(prices):
    # append 연산은 list 길이가 길어질수록 너무 시간이 오래걸리기 때문에 미리 0으로 채우고 시작
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
