# 내적

def solution(a, b):
    answer = 0
    for i, j in zip(a, b):
        answer += i * j
    return answer


# print(solution(a=[1, 2, 3, 4], b=[-3, -1, 0, 2]))


# 음양 더하기
# 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs
def solution2(absolutes, signs):
    return sum([i if j else -i for i, j in zip(absolutes, signs)])


# print(solution2(absolutes=[4, 7, 12], signs=[True, False, True]))


# 없는 숫자 더하기
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return
# 0~9까지 합은 45
def solution3(numbers):
    return sum([x for x in range(1, 10)]) - sum(numbers)


# print(solution3(numbers=[5, 8, 4, 0, 6, 7, 9]))


# 크레인 인형뽑기 게임
# 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때,
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return

def solution4(board, moves):
    answer = 0
    stacks = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1]:
                if stacks and stacks[-1] == board[j][i - 1]:
                    stacks.pop()
                    answer += 2
                else:
                    stacks.append(board[j][i - 1])
                board[j][i - 1] = 0
                break

    # print('남은 스택::', stacks)
    return answer


# print(solution4(board=[[0, 0, 0, 0, 0],
#                        [0, 0, 1, 0, 3],
#                        [0, 2, 5, 0, 1],
#                        [4, 2, 4, 4, 2],
#                        [3, 5, 1, 3, 1]],
#                 moves=[1, 5, 3, 5, 1, 2, 1, 4]))


# [카카오 인턴] 키패드 누르기
# keypad 형태를 변경 -> n 해당하는 값이 어느 좌표에 있는지 알기 위해.
def solution5(numbers, hand):
    answer = ''
    lxy, rxy = [0, 3], [2, 3]
    keypad = [[1, 4, 7, '*'],
              [2, 5, 8, 0],
              [3, 6, 9, '#']]

    for n in numbers:
        if n in keypad[0]:
            answer += 'L'
            lxy = [0, keypad[0].index(n)]
        elif n in keypad[2]:
            answer += 'R'
            rxy = [2, keypad[2].index(n)]
        else:
            keyxy = [1, keypad[1].index(n)]
            l, r = 0, 0
            for i in range(2):
                l += abs(lxy[i] - keyxy[i])
                r += abs(rxy[i] - keyxy[i])

            if (l == r and hand == 'right') or (l > r):
                answer += 'R'
                rxy = [1, keypad[1].index(n)]
            else:
                answer += 'L'
                lxy = [1, keypad[1].index(n)]

    return answer


print(solution5(numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], hand="right"))


# 다른 사람의 풀이
# 키패드를 dict 형태로 저장
# def solution_other_tmp(numbers, hand):
#     key_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
#                 4: (1, 0), 5: (1, 1), 6: (1, 2),
#                 7: (2, 0), 8: (2, 1), 9: (2, 2),
#                 '*': (3, 0), 0: (3, 1), '#': (3, 2)}
#     for i in numbers:
#         curPos = key_dict[i]
#         lPos = key_dict[i]
#         rPos = key_dict[i]
#         ldist = abs(curPos[0] - lPos[0]) + abs(curPos[1] - lPos[1])
#         rdist = abs(curPos[0] - rPos[0]) + abs(curPos[1] - rPos[1])




