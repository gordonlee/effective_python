"""

23. 인터페이스가 간단하면 클래스 대신 함수를 받자.

"""
from collections import defaultdict
"""
일급 함수(first-class function)? # 원래 이런 이름이 맞나 싶다..
: 함수 안에 함수가 존재, 변환값이 함수
그냥 delegate 랑 다를 게 없는데;
참고: http://forarchitect.tistory.com/54
"""

# 간단한 사용자 sort 예제
names = ['aaa', 'bbbb', 'cc', 'dddddddddd']
names.sort(key=lambda x: len(x))
print(names)


# default dict 에 찾을 수 없는 키에 접근할 때마다 호출된 함수를 줄 수 있다.
def log_missing():
    print('key added')
    return 0

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]
result = defaultdict(log_missing, current)
print('Before: {0}'.format(dict(result)))
for key, amount in increments:
    result[key] += amount
print('After: {0}'.format(dict(result)))


# added_count 가 필요하면 아래처럼 처리할 수도 있다. (함수 묶음도 살짝 바뀜)
def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count  # 상태 보존 클로저
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2


# 별도의 작은 클래스를 만들어서 가독성을 향상시키는 방법
class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = None
result = defaultdict(counter.missing, current)

for key, amount in increments:
    result[key] += amount
print('added: {0}'.format(counter.added))


# MEMO: __call__ method? CH23_appendix_special_method_names.py
# __call__ method 를 이용한 방법
class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
counter()
assert callable(counter)

counter = BetterCountMissing()
result = defaultdict(counter, current)

print('Before: {0}'.format(dict(result)))
for key, amount in increments:
    result[key] += amount
print('added: {0}'.format(counter.added))
print('After: {0}'.format(dict(result)))
