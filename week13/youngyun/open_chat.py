def solution(record):
    c = []
    uid2nick = dict()
    result = []
    for command in record:
        t_command = command.split()
        if t_command[0] != "Leave":
            t_c, t_id, t_nick = t_command
        else:
            t_c, t_id = t_command
        if t_c == "Enter" or t_c == "Change":
            uid2nick[t_id] = t_nick
        if t_c == "Change":
            continue
        c.append([t_c, t_id])

    for r_c in c:
        if r_c[0] == "Enter":
            result.append(f"{uid2nick[r_c[1]]}님이 들어왔습니다.")
        elif r_c[0] == "Leave":
            result.append(f"{uid2nick[r_c[1]]}님이 나갔습니다.")

    return result


print(
    solution(
        [
            "Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan",
        ]
    )
)
