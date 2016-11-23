"""

33. 메타클래스로 서브클래스를 검증하자.

핵심 정리:
    - 서브클래스 타입의 객체를 생성하기에 앞서 서브 클래스가 정의 시점부터
      구성되었음을 보장하려면 메타 클래스를 사용하자.
    - 파이썬 2와 파이썬 3의 메타클래스 문법은 약간 다르다.(여기선 2버전은 패스)
    - 메타클래스의 __new__ 메서드는 class 문의 본문 전체가 처리된 후에 실행된다.

"""


class Meta(type):  # type 을 상속받는다.
    # (생성되는 메타 클래스, 생성될 클래스 이름, 생성될 클래스의 부모, 클래스 딕셔너리 정보)
    def __new__(mcs, name, bases, class_dict):
        print((mcs, name, bases, class_dict))
        return type.__new__(mcs, name, bases, class_dict)


class MyClass(object, metaclass=Meta):
    stuff = 123

    def __init__(self):
        self.aaa = 10

    def foo(self):
        pass


# 클래스 검증
class ValidatePolygon(type):
    def __new__(mcs, name, bases, class_dict):
        # 추상 Polygon class 는 검증하지 않음
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(mcs, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None  # 서브 클래스에서 설정

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


print('Before class')
class Line(Polygon):
    print('Before sides')
    sides = 1  # Error!
    print('After sides')
print('After class')


"""
인스턴스를 생성하는 시점이 아니라, class 를 선언하는 시점에 validation 체크가 되는 모양이다.
좀 러프하게 막히는 감이 없지 않다.
__init__ 안에서 생성하는 멤버 변수는 체크할 수 없다.
(당연한 것이 __new__를 하기 전에 if 로 체크하기 때문에 인스턴스 생성 후에 포함되는 값을 알 수 없어 보인다.)
"""
