"""

29. 게터와 세터 메서드 대신에 일반 속성을 사용하자.

요약:
    - 간단한 공개 속성을 사용하여 새 클래스 인터페이스를 정의하고
      세터와 게터 메서드는 사용하지 말자.
    - 객체의 속성에 접근할 때 특별한 동작을 정의하려면 @property 를 사용하자.
    - @property 메서드에서 최소 놀람 규칙(rule of least surprise)을 따르고
      이상한 부작용은 피하자.
    - @property 메서드가 빠르게 동작하도록 만들자.
      느리거나 복잡한 작업은 일반 메서드로 하자.

# rule of least surprise?
https://en.wikipedia.org/wiki/Principle_of_least_astonishment
A 를 get 하는데, B 를 수정하지 마라 뭐 이런 얘기.. 일관된 코드를 가져가라..

"""


# 다른 프로그래밍 언어에선 일반적이지만, 파이썬 스럽지 못한 방법이다.
class OldResistor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms

r0 = OldResistor(50e3)
r0.set_ohms(10e3)


# 공개 속성을 이용하면 아래모양이 된다.
class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

r1 = Resistor(50e3)
r1.ohms = 10e3
r1.ohms += 5e3


# 특수 동작을 위한 property 이용
class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

r2 = VoltageResistance(1e3)
print('Before: {0} amps'.format(r2.current))
r2.voltage = 10
print('After : {0} amps'.format(r2.current))


# 조건을 걸어서 체크할 수도 있다.
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property  # 부모 클래스에 self.ohms 를 사용하고 있지만, 하위 클래스가 이름을 가리는 것으로 보인다.
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('{0} ohms must be > 0'.format(ohms))
        self._ohms = ohms  #FIXME: 이건 어떻게 수정하지??

r3 = BoundedResistance(1e3)
# r3.ohms = 0


# 부모 클래스의 속성을 불변(immutable)으로 만드는 데도 사용할 수 있다.
class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms  #FIXME: 이건 어떻게 수정하지??

r4 = FixedResistance(1e3)
# r4.ohms = 2e3


# 주의사항: 게터 프로퍼티 메서드에서 다른 속성을 설정하지 말아야 한다.
class MysteriousResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        # 읽을 때(get) 여기가 실행되므로, self.voltage 가 변경됨.
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

r7 = MysteriousResistor(10)
r7.current = 0.01
print('Before: {0}'.format(r7.voltage))
r7.ohms
print('After : {0}'.format(r7.voltage))

"""
MEMO:(내생각)
부모에서 self.ohms 를 썼어도, 실제 인스턴스가 property 로 처리해놨기 때문에
자식 생성자 -> 부모 생성자(super().__init__) -> 자식의 property setting 순서로
코드 흐름이 진행된다. 실제 내부에 변수는 self.ohms, self._ohms 가 잡히는 것으로
디버거에 보이지만, 부모의 self.ohms 에 접근할 수 있는 방법이 없어진 것 같다.
애초에 이렇게 헷갈리게 안해놓는게 가장 좋긴 하겠다.
"""
