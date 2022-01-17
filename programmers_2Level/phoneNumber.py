# 전화번호 목록

# str2.startswith(str1) str1이 str2로 시작할 때, True를 아닌 경우 False를 반환
# endswith 함수는 str1이 str2로 끝날 때

def solution(phone_book):
    phone_book.sort()
    print(phone_book)

    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
                return False
    
        # 효율성 탈락
        # for j in phone_book[i+1:]:
        #     map[j[:len(phone_book[i])]] = j
        #
        #     if phone_book[i] in map:
        #         return False

    return True


# print(solution(phone_book=["119", "97674223", "1195524421"]))
print(solution(phone_book=["123", "456", "789"]))
print(solution(phone_book=["12", "123", "1235", "567", "88"]))
print(solution(phone_book=["119", "114", "112", "123223123", "1232231235"]))
