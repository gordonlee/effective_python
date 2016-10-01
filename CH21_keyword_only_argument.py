"""

21. 키워드 전용 인수(keyword-only argument)로 명료성을 강요하자.

: 함수를 호출하는 쪽에서 의도를 명확히 드러내도록 요구하는 방법으로
호출자가 꼭 위치 인수가 아닌 키워드 인수로만 호출하도록 한다.

"""


def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

safe_division_c(1, 10**500, True, False)  # Error

safe_division_c(1, 0, ignore_zero_division=True)  # No Error
"""
문법은 인수에 , *, 하위부터 적용된다.
그리고 후출부에서 꼭 모든 인수를 설정해야 하는 것은 아니다.(디폴트값이 있으니까)
위 예제처럼 옵션 자체가 매우 많아서 서로 오해의 소지가 있을 경우
사용하면 좋은 방법이 될 것 같다.
"""

# 참고: 파이썬2에는 키워드 전용 인수 문법은 없다.
"""
그래서 아래와 같은 방법으로 풀어낸다.
def safe_division_d(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_div = kwargs.pop('ignore_zero_div', False)
    if kwards:
        raise TypeError('Unexpected **kwargs: %r' % kwargs)
    # ...
"""
