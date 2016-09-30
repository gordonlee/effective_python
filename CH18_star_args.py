"""

18. 가변 위치 인수로 깔끔하게 보이게 하자.

"""


# 가변 인수가 아닌 형태의 함수
def log(message, values):
    if not values:
        print(message)
    else:
        print('{0} type: {1}'.format(type(values), values))
        values_str = ', '.join(str(x) for x in values)
        print('{0}: {1}'.format(message, values_str))

print('## 가변 인수가 아닌 형태의 함수')
log('My numbers are ', [1, 2])
log('Hi there', [])
# log('Hi there')  # Error! values 파라메터가 아예 없으므로.. 호출 자체가 에러


# 가변 인수를 이용한 형태의 함수
def log_star_args(message, *values):  # 유일하게 변경된 부분
    if not values:
        print(message)
    else:
        print('{0} type: {1}'.format(type(values), values))
        values_str = ', '.join(str(x) for x in values)
        print('{0}: {1}'.format(message, values_str))

print('## 가변 인수를 이용한 형태의 함수')
log_star_args('My numbers are ', 1, 2)
log_star_args('Hi there')


# 거꾸로 호출부에서 리스트를 갖고 있는 상태에서 가변 인수 형태로 호출하려고 할땐
# 호출부에서 * 를 붙이면 된다.
favorites = [7, 23, 293]
log_star_args('Favorite colors', favorites)
log_star_args('Favorite colors', *favorites)
"""
이 방법에는 두 가지 고려해야 할 문제가 있다.

    1) 가변 인수가 함수에 전달되기에 앞서 항상 튜플로 변환된다는 점이다.
    이는 함수를 호출하는 쪽에서 generator 에 * 연산자를 쓰면, generator 가
    모두 소진될 때까지 순회됨을 의미한다. 결과로 만들어지는 튜플은 generator 로
    부터 생성된 모든 값을 담으므로 메모리 이슈가 발생할 수 있다.

    2) *args 를 사용하고 나면, 인자가 추가될 때, 호출부를 모두 바꿔야 한다.
    게다가 예외가 발생하면 찾기가 어렵다. (21장에서 어떻게 보완할지 알아보자)
"""


# generator -> tuple 로 풀리는 과정
def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)

print('## generator -> tuple 로 풀리는 과정')
it = my_generator()
# what_is_star_args = *it  # 이렇게 풀어볼 수가 없다.. 신텍스 에라
my_func(*it)
