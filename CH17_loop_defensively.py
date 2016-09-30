"""

17. 인수를 순회할 때는 방어적으로 하자.

- 입력 인수를 여러 번 순회하는 함수를 작성할 때 주의하자.
  입력 인수가 이터레이터라면 이상하게 동작해서 값을 잃어버릴 수 있다.
- 파이썬의 이터레이터 프로토콜은 컨테이너와 이터레이터가 내장 함수 iter, next 와
  for 루프 및 관련 표현식과 상호 작용하는 방법을 정의한다.
- __iter__ 메서드를 제너레이터로 구현하면 자신만의 이터러블 컨테이너 타입을
  쉽게 정의할 수 있다.
- 어떤 값에 iter 를 두 번 호출했을 때 같은 결과가 나오고 내장 함수 next 로 전진
  시킬 수 있다면 그 값은 컨테이너가 아닌 이터레이터다.

"""


# 정규화 함수의 예제
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 29, 85]
percentages = normalize(visits)
print(percentages)


# 큰 입력을 위해 generator 로 변환해보자.
def normalize_iter(numbers):
    total = sum(numbers)
    for value in numbers:
        percent = 100 * value / total
        yield percent

percentages = list(normalize_iter(visits))
print(percentages)


# 파일 안에 있는 데이터를 읽어서 파싱하기
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

print('## 파일 안에 있는 데이터를 읽어서 파싱하기')
it = read_visits('./_data/visits_numbers.txt')
# 책엔 아래 처럼 나와있는데, it 은 generator 이므로 값을 가져올 수 없음
# percentages = normalize(list(it))  # 이렇게 하면 메모리에 다 올려서 처리 가능
percentages = normalize(it)
print(percentages)

# generator 의 소멸 예제
print('## generator 의 소멸 예제')
it = read_visits('./_data/visits_numbers.txt')
print(list(it))  # it 이 처음으로 돌아가 있을 때, 여기는 유효함
print(list(it))  # 이미 it 이 끝까지 돌아갔기 때문에, 무효한 값 출력, 예외 X


# 위와 비슷한 방법이지만, it 을 받아서 복사하는 방식을 구현한 함수
def normalize_copy(iterator):
    numbers = list(iterator)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

print('## it 을 받아서 복사하는 방식을 구현한 함수')
it = read_visits('./_data/visits_numbers.txt')
percentages = normalize_copy(it)
print(percentages)
"""
위 처럼 처리할 경우, 결국 iterator 로 받아온 모든 값을 순회하면서
list 에다 밀어넣는 작업을 하게 되는 형태다.
여전히 메모리 고갈 문제가 등장할 수 있다.
"""


# 메모리 고갈 방지를 위해 매번 새 이터레이터를 반환하게 변경
# MEMO: get_iter 는 함수형태(lambda)
def normalize_func(get_iter):
    total = sum(get_iter())  # 새 이터레이터 <-- 초기 이터레이터를 받아서 처리
    result = []
    for value in get_iter():  # 새 이터레이터 <-- 초기 이터레이터를 받아서 처리
        percent = 100 * value / total
        result.append(percent)
    return result

print('## 메모리 고갈 방지를 위해 매번 새 이터레이터를 반환하게 변경')
path = './_data/visits_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
"""
sum() 와 for value in iter() 가 제대로 동작하는 이유는
내부적으로 __iter__ 가 구현되어 있으면, 루프에서 사용할 수 있다.
"""


# 클래스를 이용한 이터레이션
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

print('## 클래스를 이용한 이터레이션')
visits = ReadVisits(path)
percentages = normalize(visits)  # for value in __iter__ 로 호출됨
print(percentages)


# 파라미터가 단순한 이터레이터가 아님을 보장하는 함수
def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):  # 이터레이터 -- 거부
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
normalize_defensive(visits)  # No Error
print('{0} type, {1}'.format(type(visits), visits))
visits = ReadVisits(path)
normalize_defensive(visits)  # No Error
print('{0} type, {1}'.format(type(visits), visits))

it = iter(visits)
print('{0} type, {1}'.format(type(it), it))
# normalize_defensive(it)  # Exception occurs
"""
it을 넣는 경우는 익셉션이다. 왜냐하면 parameter 로 iterator 가 넘어오면,
iter(iterator) == iter(iterator) 이 가정이 성립하기 때문에다.
만약 list 나 클래스 중 __iter__ 가 구현되어 있는 오브젝트의 경우는
iter() 를 호출했을 때, 다음 포인터로 진행시키기 때문에 값이 같아질 수 없다.
"""


# iterator 인스턴스와 iter 함수에 대한 이해
print('iterator 인스턴스와 iter 함수에 대한 이해')

"""
타입은 모두 list_iterator 이지만, 5번부터 iter() 함수안에 파라메터를
list 대신 iterator 를 넣었다. 이 경우 4, 5, 6이 모두 동일한 주소값을
갖는 동일 포인터가 출력되었다.
이와 같은 원리를 이용해서 normalize_defensive() 함수의 익셉션 발생 조건을
이해할 수 있다.
"""
list_instance = [1, 2, 3, 4, 5, 6]

it = iter(list_instance)
# 1) <class 'list_iterator'> type, <list_iterator object at 0x02315490>
print('{0} type, {1}'.format(type(it), it))

it = iter(list_instance)
# 2) <class 'list_iterator'> type, <list_iterator object at 0x023154D0>
print('{0} type, {1}'.format(type(it), it))

it = iter(list_instance)
# 3) <class 'list_iterator'> type, <list_iterator object at 0x02315430>
print('{0} type, {1}'.format(type(it), it))

it = iter(list_instance)
# 4) <class 'list_iterator'> type, <list_iterator object at 0x02315490>
print('{0} type, {1}'.format(type(it), it))

it = iter(it)
# 5) <class 'list_iterator'> type, <list_iterator object at 0x02315490>
print('{0} type, {1}'.format(type(it), it))

it = iter(it)
# 6) <class 'list_iterator'> type, <list_iterator object at 0x02315490>
print('{0} type, {1}'.format(type(it), it))


# iterator vs generator
# ref: http://anandology.com/python-practice-book/iterators.html
