import re


def remove_dot(string):
    result = ""
    dot_flag = False
    for c in string:
        if c == "." and dot_flag == True:
            continue

        if c == ".":
            dot_flag = True
        else:
            dot_flag = False
        result += c

    result = result.lstrip(".")
    result = result.rstrip(".")
    return result


def solution(new_id):
    answer = new_id.lower()  # 1
    answer = re.sub(r"[^0-9a-z_-.]", "", answer)  # 2
    answer = remove_dot(answer)  # 3, 4
    if not answer:
        answer = "a"  # 5
    if len(answer) >= 16:
        answer = answer[:15]  # 6
        answer = answer.rstrip(".")  # 7
    if len(answer) <= 2:
        c = answer[-1]
        while len(answer) < 3:
            answer += c

    print(answer)
    return answer
