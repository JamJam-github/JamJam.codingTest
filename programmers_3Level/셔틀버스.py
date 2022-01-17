from datetime import datetime, timedelta


def solution(n, t, m, timetable):
    answer = ''
    new_timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    new_timetable.sort()
    # print('new_timetable', new_timetable)

    # n번, t분 간격, 최대 m명
    # time = datetime.strptime("09:00", "%H:%M")
    bus_table = [540]
    # for i in range(n - 1):
    #     time += timedelta(minutes=t)
    #     bus_table.append(time.hour * 60 + time.minute)
    bus_table = [540 + (t * i) for i in range(n)]
    # print('bus table', bus_table)

    # 버스 시간에 정원이 가득차면 마지막 크루 -1분
    # 버스 시간에 정원이 가득차지 않으면 마지막 버스시간
    bus_idx = 0
    while bus_idx < len(bus_table):
        bus_stack = []
        count = 0
        while count != m:
            if new_timetable and new_timetable[0] <= bus_table[bus_idx]:
                bus_stack.append(new_timetable.pop(0))
                count += 1
            else:
                break

        bus_idx += 1
        # 마지막 버스에서 체크
        if bus_idx == len(bus_table):
            if len(bus_stack) == m:
                answer = bus_stack[-1] - 1
            else:
                answer = bus_table[-1]
            break

    return "{:02d}:{:02d}".format(answer // 60, answer % 60)


print(solution(n=1, t=1, m=5, timetable=["08:00", "08:01", "08:02", "08:03"]))
print(solution(n=2, t=10, m=2, timetable=["09:10", "09:09", "08:00"]))
print(solution(n=2, t=1, m=2, timetable=["09:00", "09:00", "09:00", "09:00"]))
print(solution(n=1, t=1, m=1, timetable=["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(n=1, t=1, m=1, timetable=["23:59"]))
print(solution(n=10, t=60, m=45,
               timetable=["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                          "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))


# 다른 사람의 풀이
def solution_other(n, t, m, timetable):
    timetable = [int(i[:2]) * 60 + int(i[3:]) for i in timetable]
    timetable.sort()
    bustable = [9 * 60 + t * i for i in range(n)]
    for i in bustable:
        passenger = [p for p in timetable if p <= i]
        if i == bustable[-1]:
            if len(passenger) >= m:
                answer = passenger[m - 1] - 1
            elif len(passenger) < m:
                answer = i
            else:
                answer = passenger[-1]
        elif len(passenger) < m:
            timetable = timetable[len(passenger):]
        elif len(passenger) >= m:
            timetable = timetable[m:]
    answer = str(divmod(answer, 60)[0]).rjust(2, '0') + ':' + str(divmod(answer, 60)[1]).rjust(2, '0')
    return answer
