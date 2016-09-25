"""

15. 클로저가 변수 스코프와 상호 작용하는 방법을 알자.

* 클로저(closure): 자신이 정의된 스코프에 있는 변수를 참조하는 함수


"""


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
print(numbers)
sort_priority(numbers, group)
print(numbers)


# 아래는 closure 변수를 변경하는 예제이다.
def sort_priority(values, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found

print(numbers)
found = sort_priority(numbers, group)
print('found = {0}'.format(found))
print(numbers)
# 왜 여기서 found 가 False 일까?
"""
표현식에서 변수를 참조할 때, 파이썬 인터프리터의 스코프 탐색 우선순위
     1. 현재 함수의 스코프
     2. (현재 스코프를 담고 있는 다른 함수 같은 감싸고 있는 스코프
     3. 코드를 포함하고 있는 모듈의 스코프(전역 스코프라고도 함)
     4. (len 이나 str 같은 함수를 담고 있는) 내장 스코프
위 내용에서 찾지 못하면, NameError 예외가 발생한다.

그러나, 변수 할당은 다른 로직으로 돌아간다. (found 가 False 인 이유)
변수가 이미 현재 스코프에 정의되어 있다면 새로운 값을 얻는다.
새로 정의되는 변수의 스코프는 그 할당을 포함하고 있는 함수가 된다.
"""

# closure 에서 상위 스코프의 값을 바꾸려고 한다면, nonlocal 키워드를 사용할 수 있다.
def sort_priority(values, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found

print(numbers)
found = sort_priority(numbers, group)
print('found = {0}'.format(found))
print(numbers)
# 위 처럼 nonlocal 은 코드가 커지면 점점 디버깅이 어려워지는 단점이 있다.

# 아래 코드는 약간 더 길지만, 이해하가는 더 편하다.
class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sorter(group)
numbers.sort(key= sorter)
assert sorter.found is True
