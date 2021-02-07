from itertools import combinations

def filtering_course(orders, course):
    remove_idx = []
    len_orders = list(map(len, orders))
    for i, c in enumerate(course):
        if sum([el >= c for el in len_orders]) < 2:
            remove_idx.append(i)
            
    for idx in sorted(remove_idx, reverse=True):
        del course[idx]
    
    return course

def get_combis(l, cs):
    combis_list = []
    for c in cs:
        combis_list.append({k: 0 for k in list(map(''.join, combinations(l, c)))})
    return combis_list

def num_contains(cmpers, cmpee):
    return sum([all(x in cmper for x in cmpee) for cmper in cmpers])
    # return all(x in cmper for x in cmpee)  # 모든 cmpee는 cmper에 있다.
    
def solution(orders, course):
    answer = []
    
    # 모든 문자열 중복 없이 concat = recipe_set
    recipe_set = ''.join(sorted(list(set(''.join(orders)))))
    
    # orders 기준 2개 이상 포함될 수 없는 course를 filtering
    filtered_course = filtering_course(orders, course)
    
    # 이것을 dictionary로 만듦 = recipe_dict
    recipe_dicts = get_combis(recipe_set, filtered_course)
    
    for recipe_dict in recipe_dicts:
        # recipe_dict의 value를 order에 포함된 개수만큼 올림
        for r in recipe_dict.keys():
            recipe_dict[r] = num_contains(orders, r)
    
    # 각 recipe_dict를 정렬 후, 최대값을 같는 key들을 answer에 저장
    for recipe_dict in recipe_dicts:
        max_n = max(list(recipe_dict.values()))
        if max_n >= 2:
            answer += list(dict(filter(lambda elem: elem[1] == max_n, recipe_dict.items())).keys())
    
    return list(sorted(answer))
