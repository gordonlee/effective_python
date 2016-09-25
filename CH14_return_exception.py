"""

14. None 을 반환하기보다는 예외를 일으키자

"""


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

x, y = 1, 2

# 이렇게 사용할 수 있다.
result = divide(x, y)
if result is None:
    print("invalid inputs")

# 그런데 사용자가 ch04를 적용하여 결과평가를 해버린다면?
result = divide(x, y)
if not result:
    print("invalid inputs")
# 위 구문은 잘못된 상황이다. x가 0인 경우는 암시적 평가가 False 이므로
# 잘못된 결과가 출력된다. (실제 계산 결과가 0임)

# 이런 케이스에서는 리턴할 때, 1) tuple 로 묶어서 (함수 성공/실패, 결과 값)을 던져주거나
# 2) ZeroDivisionError 예외를 잡아서, InvalidError 예외로 바꿔주는 방법이 있다

# 1번 예제 (사용자가 예외 처리를 할 필요는 없지만, 튜플의 첫번째 값을 체크하지 않으면 문제의 소지가 있음.
def divide_1(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

# 2번 예제 (사용자가 예외처리를 다시 해야함)
def divide_2(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('invalid inputs') from e

