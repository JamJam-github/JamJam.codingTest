# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# capitalize()메소드는 첫 번째 문자를 대문자로 표시하고 나머지 문자는 소문자입니다.
# 첫 번째 문자가 이미 대문자이면 아무 작업도 수행하지 않습니다.

def solution(s):
    s = [i.capitalize() for i in s.split(' ')]
    # print(s)
    return ' '.join(s)


print(solution(s="3people unFollowed me"))
print(solution(s="for the last week"))



