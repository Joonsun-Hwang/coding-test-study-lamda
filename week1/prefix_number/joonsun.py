def solution(phone_book):
    for num in phone_book:
        for other_num in [x for x in phone_book if x is not num]:
            if num in other_num[0:len(num)]:
                return False
    return True
