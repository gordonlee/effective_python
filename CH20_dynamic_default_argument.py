"""

20. 동적 기본 인수를 지정하려면 None 과 docstring 을 사용하자.

- 기본 인수는 모듈 로드 시점에 함수 정의 과정에서 딱 한 번만 평가된다.
- 값이 동적인 키워드 인수에는 기본값으로 None을 사용하자. 그리고
  나서 함수의 docstring 에 실제 기본 동작을 문서화하자.

"""
import json


# default 인수의 잘못된 사용의 예
def decode_wrong(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode_wrong('bad data')
foo['stuff'] = 5
bar = decode_wrong('also bad')
bar['meep'] = 1
print('Foo: {0} / id: {1}'.format(foo, id(foo)))
print('Foo: {0} / id: {1}'.format(bar, id(bar)))
"""
default = {} 를 하면, 딕셔너리 객체가 매번 함수 호출마다 생성되는 것이 아니라
static 하게 처리되어 default 를 return 받은 객체는 모두 동일한 딕셔너리를 들고있게 된다.
"""


# 각자 다른 결과를 받으려면 아래와 같이 함수 내부에서 할당을 해줘야 한다.
def decode(data, default=None):
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo: {0} / id: {1}'.format(foo, id(foo)))
print('Foo: {0} / id: {1}'.format(bar, id(bar)))
