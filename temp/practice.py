

# n = int(input("Number of elements:"))
# haystack = [k for k in range(n)]
# print(haystack)
# print("searching for maximum value...")

# ts = time.time()
# maximum = max(haystack)
# elapsed = time.time() - ts
#
# print("max element = %d, Elapsed time = %.2f" % (maximum, elapsed))
import collections
from collections import Counter

L = [64, 72, 83, 72, 54]
# print(L)
# print(sorted(L, reverse=True))

A = [{'name': 'John', 'score': 83}, {'name': 'Paul', 'score': 92}]
# A.sort(key= x: x['score'], reverse=True)


# print(A)


# 상속 사용해보기
class Country:
    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드 입니다.')


class Province:
    Province_list = []

    def show(self):
        print('구 클래스의 메소드 입니다.')


# 클래스의 다중상속이 가능하며 개수 제한이 없음
class Korea(Country, Province):

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print('국가 이름은 : ', self.name)

    # 메소드 오버라이딩
    # -- Python은 오버로딩(파라미터 다른 것)이 존재하지 않음 --
    # 부모 클래스의 show()메소드는 무시되고 자식클래스의 show()메소드가 수행됩니다.
    # super 키워드로 부모메소드도 수행하고 자식메소드로 함께 출력가능
    def show(self):
        super().show()
        print(
            """
            국가의 이름은 {}입니다.
            """.format(self.name)
        )


# a = Korea('대한민국')
# a.show()
# print(Korea.mro())


# 클래스에서 직접 접근할 수 있는 정적 메소드 (classmethod와 staticmethod)
class CustomClass:

    # 인스턴스 메소드
    def add_instance_method(self, a, b):
        return a + b

    @classmethod
    def add_class_method(cls, a, b):
        return a + b

    @staticmethod
    def add_static_method(a, b):
        return a + b


# print(CustomClass.add_instance_method(None, 3, 5))
# print(CustomClass.add_class_method(3, 5))
# print(CustomClass.add_static_method(3, 5))


class Language:
    default_language = "English"

    def __init__(self):
        self.show = '나의 언어는 ' + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()

    def print_language(self):
        print(self.show)


class KoreanLanguage(Language):
    default_language = '한국어'


# staticmethod는 부모클래스의 클래스속성 값을 가져오지만
# classmethod는 cls인자를 활용하여 cls의 클래스속성을 가져온다
a = KoreanLanguage.static_my_language()
b = KoreanLanguage.class_my_language()
# a.print_language()
# b.print_language()


# 덕 타이핑
class Parrot:
    def fly(self):
        print("Parrot flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

class Whale:
    def swim(self):
        print("Whale flying")


def lift_off(entity):
    entity.fly()


parrot = Parrot()
airplane = Airplane()
whale = Whale()

# lift_off(parrot)
# lift_off(airplane)


# collections 모듈
# 합집합 Union 문법: c1 | c2
# In-place Union 문법: c1 |= c2

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

print(portfolio)

total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] = total_shares[name] + shares

print(total_shares)
print(total_shares['IBM'])

print()
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
answer1 = collections.Counter(participant)
answer2 = collections.Counter(completion)
print('part ::', answer1)
print('comp ::', answer2)
print('part - comp ::', answer1 - answer2)
print('part - comp ::', (answer1 - answer2).keys())
