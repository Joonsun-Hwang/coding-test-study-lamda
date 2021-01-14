def solution(phone_book):
    for number in range(len(phone_book)) :
        length = len(phone_book[number])
        for book in range(len(phone_book)):
            if book == number :
                continue
            if phone_book[number] == phone_book[book][:length]:
                return False
            
    
    
    return True