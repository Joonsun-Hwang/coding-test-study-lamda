import pdb
def solution(n, words):
    history = []
    first = True
    past = ''
    for idx, w in enumerate(words):
        turn = (idx%n)+1    
        if first:
#             pdb.set_trace()
            past = w
            first = False
        else :
            if past[-1] != w[0]:
                return [turn,(idx)//n +1]
            if w in history:
                print(w)
                return [turn,(idx)//n +1]
            past = w
        history.append(w)
    return [0,0]