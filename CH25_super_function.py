"""

25. super 로 부모 클래스를 초기화하자

- 파이썬의 표준 메서드 해석 순서(MRO)는 슈퍼클래스의 초기화 순서와
다이아몬드 상속 문제를 해결한다.
- 항상 내장 함수 super 로 부모 클래스를 초기화하자.

"""
from pprint import pprint


# __init__ 를 직접 호출하여 초기화
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value
        print("MyBaseClass.__init__() => {0}".format(self.value))


class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)
        print("MyChildClass.__init__() => {0}".format(self.value))
"""
위험한 방법이다. 아래 예제를 보자.
"""


class TimesTwo(object):
    def __init__(self):
        self.value *= 2
        print("TimesTwo.__init__() => {0}".format(self.value))


class PlusFive(object):
    def __init__(self):
        self.value += 5
        print("PlusFive.__init__() => {0}".format(self.value))


# 위의 4가지 클래스를 이용하여 아래와 같은 클래스를 만들어보자.
class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

# OneWay 가 호출하는 순서
print('== OneWay ==')
foo = OneWay(5)
print('First ordering is (5 * 2) + 5 = {0}'.format(foo.value))


# 아래와 같은 케이스도 생각해보자.
class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)
"""
이 경우, AnotherWay 의 상속구문에서 mybase -> plus five -> times two 순서로
바뀌었음에도 불구하고 여전히 OneWay 클래스와 동일한 결과를 뱉는다.
"""
print('== Another ==')
foo = AnotherWay(5)
print('First ordering is (5 * 2) + 5 = {0}'.format(foo.value))


# 다이아몬드 상속 케이스
print('== 다이아몬드 상속 케이스 ==')


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5
        print("TimesFive.__init__() => {0}".format(self.value))


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2
        print("PlusTwo.__init__() => {0}".format(self.value))
# 이 두 클래스 모두에서 상속받는 자식 크래래스를 정의하여 MyBaseClass 를 다이아몬드의 꼭대기로 만든다.


class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)

foo = ThisWay(5)
print('Should be (5 * 5) + 2 = 27, but the result is {0}'.format(foo.value))
"""
파이썬 2.2 에서는 이 문제를 해결하려고 super 라는 내장함수를 추가하고
메서드 해석 순서(MRO, Method Resolution Order)를 정의했다.
(깊이 우선, 왼쪽에서 오른쪽으로)
"""


# 파이썬2
class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


foo = GoodWay(5)
print('Should be 5 * (5 + 2) = 35 and the result is {0}'.format(foo.value))
"""
init 의 실행되는 순서를 바꿀 순 없다. MRO 순서대로 동작한다.
MRO 는 class.mro() 를 호출하면 얻을 수 있다.
"""
pprint(GoodWay.mro())
print(GoodWay.mro())


"""
super 를 인수없이 호출하면 __class__와 self 를 인수로 넘겨서 호출한 것으로 처리해서
이 문제를 해결한다. 파이썬3에서는 항상 super 를 사용해야 한다.
"""


# 파이썬3
class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)


class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)


assert Explicit(10).value == Implicit(10).value
