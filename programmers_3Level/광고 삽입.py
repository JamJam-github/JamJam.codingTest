# "죠르디" 동영상의 총 재생시간은 02시간 03분 55초 입니다.
# "죠르디"의 동영상 재생시간 길이 play_time,
# 공익광고의 재생시간 길이 adv_time, HH:MM:SS 형식
# 시청자들이 해당 동영상을 재생했던 구간 정보 logs가 매개변수로 주어질 때
# 시청자들의 누적 재생시간이 가장 많이 나오는 곳에 공익광고를 삽입하려고 합니다.
# 이때, 공익광고가 들어갈 시작 시각을 구해서 return 하도록 solution 함수를 완성해주세요.

# Memorizaion 문제
# 완전 탐색

def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:])
    return hour + minute + second


def get_timeformat(time):
    hour = time // 3600
    minute = (time % 3600) // 60
    second = time % 60
    return str(hour).rjust(2, '0') + ":" + str(minute).rjust(2, '0') + ":" + str(second).rjust(2, '0')


def solution(play_time, adv_time, logs):
    play_sec = get_time(play_time)
    adv_sec = get_time(adv_time)
    # print('play_sec::', play_sec, 'adv_sec::', adv_sec)

    # 초로 변환
    total = [0 for _ in range(play_sec + 1)]
    for log in logs:
        slog, elog = log.split('-')
        start = get_time(slog)
        end = get_time(elog)

        # 매번 누적하면 for 크기가 크면 시간이 오래걸려서
        # 마킹 후 1회 순회해서 누적하는 방법으로 변경
        # for j in range(start, end):
        #     total[j] += 1
        total[start] += 1
        total[end] -= 1

    for i in range(1, play_sec):
        total[i] += total[i - 1]
    # print('total>>', total[1550], total[2431])

    # 광고를 삽입할 수 있는 구간은 처음부터 넣을 수 있음.
    # init 광고 구간 인덱스 1부터 광고 총 시간까지
    currSum = sum(total[:adv_sec])
    maxSum = currSum
    # print('초기 sum::', currSum)

    adv_start = 0
    for i in range(adv_sec, play_sec):
        currSum += (total[i] - total[i - adv_sec])
        if maxSum < currSum:
            maxSum = currSum
            adv_start = i - adv_sec + 1

    answer = get_timeformat(adv_start)
    return answer


print(solution(play_time="02:03:55", adv_time="00:14:15",
               logs=["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29",
                     "01:30:59-01:53:29", "01:37:44-02:02:30"]))
