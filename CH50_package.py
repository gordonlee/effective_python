"""

50. 모듈을 구성하고 안정적인 API 를 제공하려면 패키지를 사용하자.

파이썬에서 패키지란?
    다른 모듈을 포함하는 모듈을 말한다.

대부분 디렉터리 안에 __init__.py 라는 빈 파일을 넣는 방법으로 패키지를 정의한다.
__init__.py 가 있으면 해당 디렉터리에 있는 다른 파이썬 파일은 상대적인 경로로
임포트 할 수 있다.

패키지의 주요 목적
    - 네임스페이스: 모듈들을 분할. 파일 이름이 같은 여러 모듈이 서로
    다른 절대 경로를 갖게 해준다.
    - 안정적인 API: 릴리즈 간의 변경 없이 안정적인 기능을 제공하고 싶을 때,
    때론 외부 사용자에게서 내부 코드 구조를 숨겨야 한다.(?)

* __all__ :
이 값은 공개 API 의 일부로 외부에서 제공하려는 모듈 이름을 모두 담은 리스트.

* 주의: import *
    - from foo import * 는 코드를 처음 보는 사람에게 이름의 출처를 숨긴다.
    - import * 문으로 가져온 이름은 이 문자를 포함하는 모듈 내에서 충돌하는
    이름을 덮어쓴다.

핵심 정리
    - 패키지를 이용하면 고유한 절대 모듈 이름으로 코드를 분리하고, 충돌하지
    않는 네임스페이스를 구성할 수 있다.
    - 간단한 패키지는 다른 소스 파일을 포함하는 디렉터리에 __init__.py 파일을
    추가하는 방법으로 정의한다.
    - __all__ 이라는 특별한 속성에 공개하려는 이름을 나열하여 모듈의 명시적
    API 를 제공할 수 있다.
    - 공개할 이름만 패키지의 __init__.py 파일에서 임포트하거나 내부 전용 멤버의
    이름을 밑줄로 시작하게 만들면 패키지의 내부 구현을 숨길 수 있다.
    - 단일 팀이나 단일 코드 베이스로 협업할 때는 외부 API 용으로 __all__ 을
    사용할 필요가 없을 것이다.

"""

from CH50_package_sample import utils
from CH50_package_sample.analysis import utils  # 위 import 를 얘가 덮어씀!

print(utils.util_func_a())

"""
이런 덮어씀 문제는 as 절을 이용해서 해결할 수 있다.
"""

from CH50_package_sample import utils as root
from CH50_package_sample.analysis import utils as analysis

print(root.util_func_a())
print(analysis.util_func_a())

from CH50_package_sample import *
a = Projectile(1.5, 3)
b = Projectile(4, 1.7)
result = simulate_collision(a, b)

print('**********************************************************')
help("CH50_package_sample")
"""RESULT of help("CH50_package_sample")
Help on package CH50_package_sample:

NAME
    CH50_package_sample

PACKAGE CONTENTS
    models
    utils

SUBMODULES
    analysis

CLASSES
    builtins.object
        CH50_package_sample.models.Projectile

    class Projectile(builtins.object)
     |  Methods defined here:
     |
     |  __init__(self, mass, velocity)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    simulate_collision(a, b)

DATA
    __all__ = ['Projectile', 'simulate_collision']

FILE
    d:\github\study_effective_python\ch50_package_sample\__init__.py

"""
