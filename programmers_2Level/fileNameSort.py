# [3차] 파일명 정렬

# 파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다.
# 파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다.
# 두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다.

import re


def solution(files):
    for idx, file in enumerate(files):
        # text = re.findall('\D+', file)
        # head = text[0]
        # tail = text[1]
        number = re.findall('\d+', file)[0]

        text = file.replace(number, '|', 1)
        head = text.split('|')[0]
        tail = text.split('|')[1]
        files[idx] = [head, number, tail]

    sort_files = sorted(files, key=lambda x: (x[0].lower(), int(x[1])))
    # print(sort_files)

    return [''.join(i) for i in sort_files]


# print(solution(files=["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(files=["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(files=["abc123defg123.jpg", "abc124defg123.jpg"]))


# 다른 사람의 풀이
# 첫 번째 나오는 숫자로 정렬 후
# 숫자를 기준으로 나눈 후 첫 번째 문자를 기준으로 정렬하여 리턴한다.
def solution_other(files):
    a = sorted(files, key=lambda file: int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file: re.split('\d+', file.lower())[0])
    return b
