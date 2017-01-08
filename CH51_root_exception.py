"""

51. 루트 Exception 을 정의해서 API 로부터 호출자를 보호하자.

파이썬은 표준 라이브러리용 내장 예외를 갖추고 있다. 그러나, API 를 제작할 때는
자신만의 커스텀 타입을 정의하는 편이 더 강력하게 예외를 핸들링 할 수 있다.

핵심정리
    - 작성중인 모듈에 루트 예외를 정의하면 API로부터 API 사용자를 보호할 수 있다.
    - 루트 예외를 잡으면 API 를 사용하는 코드에 숨은 버그를 찾는 데 도움이 될
    수 있다.
    - 파이썬 Exception 기반 클래스를 잡으면 API 구현에 있는 버그를 찾는 데
    도움이 될 수 있다.
    - 중간 루트 예외를 이용하면 API 를 사용하는 코드에 영향을 주지 않고 나중에
    더 구체적인 예외를 추가할 수 있다.

"""
import logging

# ** API **


# Exception 을 상속받은 커스텀 클래스는 사용자가 try/catch 에서 잡아낼 수 있다.
class Error(Exception):
    """Base-class for all exceptions raised by this module."""


class InvalidDensityError(Error):
    """There was a problem with a provided density value."""


class my_module(object):
    Error = Error
    InvalidDensityError = InvalidDensityError

    @staticmethod
    def determine_weight(volume, density):
        if density <= 0:
            raise InvalidDensityError('Density must be positive')

# ** user **
try:
    weight = my_module.determine_weight(1, -1)
except Error as e:
    logging.error('unexpected error: %s', e)

"""
1. 루트 예외가 있으면 호출자가 API 를 사용할 때 문제점을 이해할 수 있다.
호출자가 Error(root exception)에서 별도의 분기를 할 수 있도록 도와준다.
2. API 모듈의 코드 버그를 찾는데 도움이 된다.
의도하지 않은 예외는 API 코드에 있는 버그라고 볼 수 있다.
3. 시간이 지나 특정 환경에서 더 구체적인 예외를 제공하려고 API 를 확장할 수 있다.
"""
try:
    weight = my_module.determine_weight(1, -1)
except InvalidDensityError:
    weight = 0
except Error as e:
    logging.error('Bug in the calling code: %s', e)


try:
    weight = my_module.determine_weight(1, -1)
except InvalidDensityError:
    weight = 0
except Error as e:
    logging.error('Bug in the calling code: %s', e)
except Exception as e:
    logging.error('Bug in the API code: %s', e)
    raise


# 여기서 새로운 예외가 추가되어도 유연하게 대처할 수 있다.
class NegativeDensityError(InvalidDensityError):
    """A provided density value was negative."""


try:
    weight = my_module.determine_weight(1, -1)
except NegativeDensityError as e:
    raise ValueError('Must supply non-negative density') from e
except InvalidDensityError:
    weight = 0
except Error as e:
    logging.error('Bug in the calling code: %s', e)
except Exception as e:
    logging.error('Bug in the API code: %s', e)
    raise
