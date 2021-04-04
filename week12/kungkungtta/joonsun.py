def solution(n, words):
    answer = [0, 0]
    
    for i, word in enumerate(words):
        if i == 0:
            continue
        
        # check not word
        if len(word) <= 1:
            break
        
        # check continuity
        if words[i-1][-1] != word[0]:
            break
        
        # check duplicate
        if word in words[:i]:
            break
    else:
        return answer
    
    answer[0] = i%n+1
    answer[1] = i//n+1
    return answer
