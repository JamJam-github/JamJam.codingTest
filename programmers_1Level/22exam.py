# 2016년
# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?
# 윤년은 4로 나누어 떨어지는 년도, 즉 366일(기존 2월 28일 -> 29일까지)


a, b = 6, 30


def solution(a, b):
    weeks = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    mons = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = sum(mons[:a - 1]) + b
    print('day ::', days, '일')
    answer = weeks[((days % 7) + 4) % 7]
    return answer


print(solution(a, b))


# 다른 사람의 풀이
def getDayName(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a - 1]) + b - 1) % 7]
