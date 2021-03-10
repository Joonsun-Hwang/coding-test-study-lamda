def solution(s):
    candidate_list = []
    for cut in range(1, len(s) // 2 + 1):
        cmp_str = ""
        tmp_str = s[:cut]
        count = 1
        for idx in range(cut, len(s), cut):
            if s[idx : cut + idx] == tmp_str:
                count += 1
            else:
                if count == 1:
                    count = ""
                cmp_str += str(count) + tmp_str
                tmp_str = s[idx : cut + idx]
                count = 1
        if count == 1:
            count = ""
        cmp_str += str(count) + tmp_str
        candidate_list.append(len(cmp_str))
        print(cmp_str)
        print("cut:", cut)

    return min(candidate_list)
