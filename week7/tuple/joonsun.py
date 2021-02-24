def convert_to_list1(s):  # time: 300ms
    result = []
    row = []
    num = 0
    for i, c in enumerate(s):
        if c == '{':
            row = []
        elif c == '}':
            result.append(row)
        else:
            if c.isnumeric():
                num = num * 10 + int(c)
                if s[i+1] == ',' or s[i+1] == '}':
                    row.append(num)
                    num = 0
    return result

def convert_to_list2(s):  # time: 30ms
    l = s.split('{')
    l = [list(map(int, item.split("},")[0].split(","))) for item in l]
    return l

def solution(s):
    answer = []
    
    # for l in sorted(convert_to_list1(s[1:-1]), key = len):
    for l in sorted(convert_to_list2(s[2:-2]), key = len):
        answer.append(list(set(l) - set(answer))[0])
    
    return answer
