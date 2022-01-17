# 로그 데이터를 분석한 후 초당 최대 처리량을 계산
# 응답완료시간 S 는 고정 길이 2016-09-15 hh:mm:ss.sss 형태
# 처리시간 T는 0.1s, 0.312s, 2s 와 같이 최대 소수점 셋째 자리까지 기록하며 뒤에는 초 단위를 의미하는 s로 끝난다.
# 로그 문자열 2016-09-15 03:10:33.020 0.011s은 "오전 3시 10분 33.010초"부터 "2016년 9월 15일 오전 3시 10분 33.020초"까지
# "0.011초" 동안 처리된 요청을 의미한다. (처리시간은 시작시간과 끝시간을 포함)

from datetime import datetime, timedelta


def solution(lines):
    # 정수형으로 시간을 변환하는 코드
    def get_time(time):
        hour = int(time[:2]) * 3600
        minute = int(time[3:5]) * 60
        second = int(time[6:8])
        millisecond = int(time[9:])
        return (hour + minute + second) * 1000 + millisecond

    # 시작 시간을 구하는 코드 [01:00:04.002, 2.0s]
    def get_start_time(time, duration_time):
        n_time = duration_time[:-1]  # 's' 제외
        int_duration_time = int(float(n_time) * 1000)
        return get_time(time) - int_duration_time + 1

    answer = 0
    start_time = []  # 시작 시간과 끝나는 시간을 각각 다른 배열에 추가해준다.
    end_time = []

    for l in lines:
        temp = l.split(" ")  # ['2016-09-15', '01:00:04.002', '2.0s']
        start_time.append(get_start_time(temp[1], temp[2]))
        end_time.append(get_time(temp[1]))

    print(start_time, end_time)

    for i in range(len(lines)):  # 시작시간 ['20:59:57.053000', '20:59:58.233000']
        count = 0
        cur_end_time = end_time[i]
        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                count += 1
        answer = max(answer, count)

    # L = []
    # for l in lines:
    #     temp = l.split(' ')
    #     dt = datetime.strptime(temp[0] + temp[1], '%Y-%m-%d%H:%M:%S.%f')
    #     T = float(temp[2].replace('s', '')) * 1000000
    #     print('>>', dt, T, temp)
    #     dt2 = dt - timedelta(microseconds=T) + timedelta(microseconds=1000)
    #     L.append([dt2, dt])
    #
    # L.sort(key=lambda x: x[0])
    # answer = 0
    # for i in range(len(L)):
    #     s1, e1 = L[i][0], L[i][1]
    #     count = 0
    #     for j in range(len(L)):
    #         s2, e2 = L[j][0], L[j][1]
    #         sPlus = s1 + timedelta(microseconds=1000000) - timedelta(microseconds=1000)
    #         if (s1 <= s2 <= sPlus) or (s1 <= e2 <= sPlus) or (sPlus <= e2 and s2 <= s1):
    #             # print(f'1)start={s1.strftime("%H:%M:%S.%f")}~end={sPlus.strftime("%H:%M:%S.%f")} 사이에 있다 {s2.strftime("%H:%M:%S.%f")} ~ {e2.strftime("%H:%M:%S.%f")}')
    #             count += 1
    #     answer = max(count, answer)
    #
    #     count = 0
    #     for j in range(len(L)):
    #         s2, e2 = L[j][0], L[j][1]
    #         ePlus = e1 + timedelta(microseconds=1000000) - timedelta(microseconds=1000)
    #         if (e1 <= s2 <= ePlus) or (e1 <= e2 <= ePlus) or (ePlus <= e2 and s2 <= e1):
    #             # print(f'2)start={e1.strftime("%H:%M:%S.%f")}~end={ePlus.strftime("%H:%M:%S.%f")} 사이에 있다')
    #             count += 1
    #     answer = max(count, answer)

    return answer


print(solution(lines=[
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))
print()
# print(solution(lines=[
#     "2016-09-15 20:59:57.421 0.351s",
#     "2016-09-15 20:59:58.233 1.181s",
#     "2016-09-15 20:59:58.299 0.8s",
#     "2016-09-15 20:59:58.688 1.041s",
#     "2016-09-15 20:59:59.591 1.412s",
#     "2016-09-15 21:00:00.464 1.466s",
#     "2016-09-15 21:00:00.741 1.581s",
#     "2016-09-15 21:00:00.748 2.31s",
#     "2016-09-15 21:00:00.966 0.381s",
#     "2016-09-15 21:00:02.066 2.62s"
# ]))
