"""

32. 지연 속성에는 __getattr__, __getattribute__, __setattr__ 을 사용하자.

용어 찾아보기:
    - 인스턴스 딕셔너리

핵심 정리
    - 객체의 속성을 지연 방식으로 로드하고 저장하려면 __getattr__ 과 __setattr__ 을 사용하자.
    - __getattr__ 은 존재하지 않는 속성에 접근할 때 한 번만 호출되는 반면에
      __getattribute__ 는 속성에 접근할 때마다 호출된다는 점을 이해하자.
    - __getattribute__ 와 __setattr__ 에서 인스턴스 속성에 직접 접근할 때
      super() (즉, object 클래스)의 메서드를 사용하여 무한 재귀가 일어나지 않게 하자.
"""


class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        print('Called __getattr__, {0}.'.format('LazyDB'))
        value = 'Value for {0}'.format(name)
        setattr(self, name, value)
        return value

data = LazyDB()
print('Before: ', data.__dict__)
print('foo: ', data.foo)  # instance.foo, 'Value for foo'
print('After: ', data.__dict__)


print('=== LoggingLazyDB ===')
class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__({0}), {1}'.format(name, 'LoggingLazyDB'))
        return super().__getattr__(name)  # self.__getattr__ 을 부르면 재귀를 타서 스택이 터진다.

data = LoggingLazyDB()
print('exists: ', data.exists)
print('foo: ', data.foo)  # 인스턴스 딕셔너리에 foo 가 없으니 __getattr__ 호출
print('foo: ', data.foo)  # 인스턴스 딕셔너리에 foo 가 이미 있으니 __getattr__ 을 호출하지 않음


print('=== getattribute ===')
class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__{0}'.format(name))
        try:
            return super().__getattribute__(name)
        except AttributeError:  # 요소가 없는 경우 뱉는 예외
            value = 'Value for {0}'.format(name)
            setattr(self, name, value)
            return value

data = ValidatingDB()
print('exists: ', data.exists)  # getattribute 는 이미 있는 요소도 호출된다.
print('foo: ', data.foo)  # getattribute 는 이미 있는 요소도 호출된다.
print('foo: ', data.foo)  # getattribute 는 이미 있는 요소도 호출된다.


print('=== Missing Property ===')
class MissingPropertyDB(object):
    def __getattr__(self, name):
        if name == 'bad_name':
            raise AttributeError('{0} is missing'.format(name))
        # ...

data = MissingPropertyDB()
# data.bad_name  # raise 발생


print('=== hasattr getattr ===')
data = LoggingLazyDB()
print('Before: ', data.__dict__)
print('foo exists', hasattr(data, 'foo'))
print('After: ', data.__dict__)
print('foo exists', hasattr(data, 'foo'))

print('=== hasattr getattribute ===')
data = ValidatingDB()
print('Before: ', data.__dict__)
print('foo exists', hasattr(data, 'foo'))
print('After: ', data.__dict__)
print('foo exists', hasattr(data, 'foo'))


class LoggingSavingDB(object):
    def __setattr__(self, name, value):
        print('Called __setattr__({0} {1})'.format(name, value))
        super().__setattr__(name, value)

print('=== setattr ===')
data = LoggingSavingDB()
print('Before : ', data.__dict__)
data.foo = 5  # Called __setattr__
print('After  : ', data.__dict__)
data.foo = 7  # Called __setattr__
print('Finally: ', data.__dict__)


class BrokenDictionaryDB(object):
    def __init__(self, data):
        self._data = {}

    def __getattribute__(self, name):
        print('Called __getattribute__({0})'.format(name))
        return self._data[name]  # data[name] => getattribute => data[name] => ... 재귀 => 스택오버플로

data = BrokenDictionaryDB({'foo': 3})
# data.foo


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        data_dict = super().__getattribute__('_data')
        return data_dict[name]  # 재귀 호출을 피하는 방법.
