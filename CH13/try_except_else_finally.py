"""

13. try/except/else/finally 에서 각 블록의 장점을 이용하자.

- finally
    : 예외가 발생해도 정리 코드를 실행하고 싶을 때 사용
- else
    : 어떤 예외를 처리하고 어떤 예외를 전달할지 명확히 하기 위해 사용

# MEMO: 이 스크립트는 실행가능하지 않다.
(주제가 예외 사항이라 예제 정도만 보고 넘어가기로 한다.)

"""

# try-except-else-finally 사용 예제
UNDEFINED = object()


def divide_json(path):
    handle = open(path, 'r+')  # IOError 가 일어날 수 있음
    try:
        data = handle.read()  # UnicodeDecodeError 가 일어날 수 있음
        op = json.loads(data)  # ValueError 가 일어날 수 있음
        value = (
            op['numerator'] /
            op['denominator']  # ZeroDivisionError 가 일어날 수 있음
        )
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)  # IOError 가 일어날 수 있음
        return value
    finally:
        handle.close()  # 항상 실행함
