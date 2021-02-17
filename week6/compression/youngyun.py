def solution(msg):    
    word_dict = {}
    answer = []
    
    for idx,char in enumerate(range(ord('A'),ord('Z')+1)):
        word_dict[chr(char)] = idx+1
    start = len(word_dict)
    while msg != "":
        for idx in range(len(msg),-1,-1):
            tmp_wrd = msg[:idx]
            if tmp_wrd in word_dict:
                next_word = msg[:idx] + msg[idx:idx+1]
                msg=msg.replace(tmp_wrd,"",1)
                answer.append(word_dict[tmp_wrd])
                start+=1
                word_dict[next_word] = start
                break
    return answer
                