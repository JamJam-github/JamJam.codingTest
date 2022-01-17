# [3차] 방금그곡

# 방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
# 네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
# 각 음은 1분에 1개씩 재생된다.

import math
from datetime import datetime


# 기억하는 멜로디 1 <= m <= 1439개
# musicinfos = [시작시간, 종료시간, 제목, 악보]
def solution(m, musicinfos):
    answer = []

    # 음악 길이 < 재생시간 then 반복재생
    # 음악 길이 > 재생시간 then 음악길이[:재생시간]
    # 일치하는 데이터가 여러 개일때 재생시간이 가장 긴 음악제목을 반환
    # C#, D#, F# 등 '#'이 붙은 음은 1단어로 처리해야 한다.

    # 종료-시작
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    musicinfos = [music.split(',') for music in musicinfos]
    # print(m)
    # print(musicinfos)

    for s, e, title, sheet in musicinfos:
        tmp = sheet[:].replace('#', '')
        start = datetime.strptime(s, "%H:%M")
        end = datetime.strptime(e, "%H:%M")
        play = int((end - start).seconds / 60)

        if len(tmp) < play:
            i = math.ceil(play / len(tmp))
            sheet *= i

        count = sheet.count('#')
        sheet = sheet[:play + count]
        # print(play, '분 재생, 원래 악보', len(tmp), '분 완성 악보', sheet, '멜로디', m)

        sheet = sheet.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

        if m in sheet:
            answer.append((play, title))

    answer.sort(key=lambda x: x[0], reverse=True)
    return answer[0][1] if answer else (None)


# print(solution(m="ABCDEFG", musicinfos=["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution(m="CC#BCC#BCC#BCC#B", musicinfos=["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution(m="ABC", musicinfos=["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution(m="CCB", musicinfos=["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]))
