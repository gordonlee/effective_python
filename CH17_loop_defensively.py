"""

17. 인수를 순회할 때는 방어적으로 하자.

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
