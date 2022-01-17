# 숫자 문자열과 영단어


def solution(s):
    answer = ''
    # eng = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    #        7: 'seven', 8: 'eight', 9: 'nine'}
    eng_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3',
                'four': '4', 'five': '5', 'six': '6',
                'seven': '7', 'eight': '8', 'nine': '9'}

    tmp = ''
    for i in s:
        if i.isalpha():
            tmp += i
            if eng_dict.get(tmp, ''):
                answer += eng_dict.get(tmp, '')
                tmp = ''
            else:
                pass
        else:
            answer += i
    return answer


print(solution(s="one4seveneight"))

# 다른 사람의 풀이
num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
           "eight": "8", "nine": "9"}


def solution_other(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
