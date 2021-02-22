def solution(skill, skill_trees):
    answer = 0
    per_skill = skill
    for sg in skill_trees:
        skill = per_skill
        for char in sg:
            if char not in skill:
                pass
            else :
                if char == skill[0]:
                    skill=skill[1:]
                else:
                    print(sg)
                    break
        else :
            answer+=1
    return answer