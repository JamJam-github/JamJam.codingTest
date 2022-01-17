from temp import main
import sys

print('1. subModule.py __name__:', __name__)  # __name__ 변수 출력
main.print_hi()


print("2. sys.argv 길이: ", len(sys.argv))

for i in sys.argv:
    print("arg value:", i)