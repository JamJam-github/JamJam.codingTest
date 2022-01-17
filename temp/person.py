class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self, other):
        print(f'{self.name} says hello to {other}.')

person = Person('solbin Choi', 28)
print(person.__dict__)

person.greet('mandoo')

# new 메소드를 이용해서 새로운 인스턴스 객체를 만든다.
# another_person = Person.__init__(another_person, 'youngchul', 34)
another_person = object.__new__(Person)
print(another_person.__dict__)
print(type(another_person))

Person.__init__(another_person, 'youngchul Park', 34)
print(another_person.__dict__)