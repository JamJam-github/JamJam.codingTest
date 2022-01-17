def print_hi():
    print(f'imported from {__name__}')


# 메인에서 메인을 불렀을 경우, 다른 파일에서 부른 경우
if __name__ == '__main__':
    print_hi()
    print(__name__)
else:
    print_hi()
    print(__name__)
