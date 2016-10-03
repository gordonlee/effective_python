"""

22. 딕셔너리와 튜플보다는 헬퍼 클래스로 관리하자.

    - 다른 딕셔너리나 긴 튜플을 값으로 담은 딕셔너리를 생성하지 말자.
    - 정식 클래스의 유연성이 필요 없다면 가벼운 불변 데이터 컨테이너에는
      namedtuple 을 사용하자.
    - 내부 상태를 관리하는 딕셔너리가 복잡해지면 여러 헬퍼 클래스를
      사용하는 방식으로 관리 코드를 바꾸자.

"""

"""
# 처음에는 학생이름-과목-점수 정도만 연결되어 있었던 요구사항이
# 지속적으로 개편되어 데이터를 처리하는 메니져 객체 함수 안에
# for 등의 반복문이 등장하게 되면,(=딕셔너리 안에 딕셔너리 등)
# 헬퍼 클래스로 리모델링 하는 편이 낫다.
"""


# MEMO: named tuple 에 대해서 알아보자.
# https://docs.python.org/3/library/collections.html#collections.namedtuple

# 최종적으로 리모델링을 한다면 아래와 같은 모습을 고려해보자.
class Grade(object):
    def __init__(self, score, weight):
        self.score = score
        self.weight = weight


class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class GradeBook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


# 위 코드를 활용한 호출부 코드
book = GradeBook()
albert = book.student('Albert Einstein')
math = albert.subject('Math')
math.report_grade(80, 0.10)

print(albert.average_grade())
