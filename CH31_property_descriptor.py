"""

31. 재사용 가능한 @property 메서드에는 디스크립터를 사용하자.

what is descriptor?
    https://docs.python.org/3/howto/descriptor.html

정리:
    - 직접 디스크립터 클래스를 정의하여 @property 메서드의 동작과 검증을 재사용하자.
    - WeakKeyDictionary 를 사용하여 디스크립터 클래스가 메모리 누수를 일으키지 않게 하자.
    - __getattribute__ 가 디스크립터 프로토콜을 사용하여 속성을 얻어오고 설정하는
      원리를 정확히 이해하려는 함정에 빠지지 말자. (그냥 쓰란 말인가;;;)

"""


class Homework(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value

galileo = Homework()
galileo.grade = 95


class ExamUsingNumeric(object):
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value


"""
위 코드는 클래스 안에 과목(인스턴스)마다 코드수가 급격히 길어진다.(프로퍼티 세팅)
장황해 지는 코드를 방지하기 위해 descriptor protocol 을 이용해보자.
"""


class Grade(object):
    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value


class Exam(object):
    # 클래스 속성
    # 여기다 쓰면 static 이다! 인스턴스 별로 하려면 여기다 쓰면 안됨.
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


exam = Exam()
exam.writing_grade = 40
# 위 코드는 아래처럼 해석된다.
# Exam.__dict__['writing_grade'].__set__(exam, 40)

exam.writing_grade
# 위 코드는 아래처럼 해석된다.
# Exam.__dict__['writing_grade'].__get__(exam, Exam)


"""
책에선 Grade 안에 여러 값을 받도록 dict 처리를 했는데,
사실 클래스 이름으로 보나 구조로 보나 Exam 이 Grade 의 dict 를 갖고 있어야
말이 맞는거 아닌가?? 맘에 별로 안들지만 일단 예제는 작성해본다.
"""


class GradeWithDict(object):
    def __init__(self):
        self._values = {}
        # self._values = WeakKeyDictionary()  # 릭 처리

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value

# memory leak 은 WeakKeyDictionary() 라는 얘로 처리할 수 있음.
