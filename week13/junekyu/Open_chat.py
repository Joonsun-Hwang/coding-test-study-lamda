
from collections import defaultdict


def solution(record):
    answer = []
    logs = defaultdict(str)
    for r in record:
        r_ = r.split(" ")
        if r_[0] == "Enter":
            logs[r_[1]] = r_[2]
        elif r_[0] == "Change":
            logs[r_[1]] = r_[2]

    for r in record:
        r_ = r.split(" ")
        if r_[0] == "Enter":
            answer.append(logs[r_[1]] + "님이 들어왔습니다.")
        elif r_[0] == "Leave":
            answer.append(logs[r_[1]] + "님이 나갔습니다.")

    return answer


def main():
    record = [
        "Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",
        "Enter uid1234 Prodo", "Change uid4567 Ryan"
    ]
    answer = solution(record)
    print(answer)
    #  ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


if __name__ == "__main__":
    main()

