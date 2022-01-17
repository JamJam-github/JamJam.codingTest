# 2개 이하로 다른 비트

# 짝수는 비트에서 마지막 비트 + 1 (혹은 그냥 다음 숫자값)
# 홀수인 경우 비트가 모두 '1'로 채워진 경우 맨 앞에 '1'을 '10'으로 변경
#           아닌 경우 '01'이 포함된 인덱스를 찾아 해당 '01'을 '10'으로 변경해주기

def solution(numbers):
    answer = []

    def bit_search(n):
        if n % 2 == 0:
            print(n, bin(n), bin(n)[:-1] + '1')
            return n + 1
        else:
            binary = format(n, 'b')
            if len(binary) == binary.count('1'):
                binary = '10' + binary[1:]
            else:
                index = binary.rfind('01')
                binary = binary[:index] + '10' + binary[index + 2:]

            return int(binary, 2)

    for n in numbers:
        answer.append(bit_search(n))

    return answer


print(solution(numbers=[2, 7]))
