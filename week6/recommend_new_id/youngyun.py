"""
-,_,. 문자만 사용할 수 있다.
만 마침표는 처음과 끝에 사용할 수 없고 연속으로 사용불가
"""
import re
import pdb


def solution(new_id):
    new_id = new_id.lower()
    #     pdb.set_trace()
    new_id = re.sub("[^\w._-]", "", new_id)
    new_id = re.sub("[.]{2,}", ".", new_id)
    new_id = new_id.strip(".")
    if new_id == "":
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id.rstrip(".")
    if len(new_id) <= 2:
        last_word = new_id[-1]
        while True:
            if len(new_id) == 3:
                break
            new_id += last_word
    new_id = new_id.strip(".")
    return new_id
