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


""" 발표 준비 """


class SimpleGradeBook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book = SimpleGradeBook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)

print(book.average_grade('Isaac Newton'))

# SimpleGradeBool <>- 1..1 -- grades: dict
# grades(name: key, score: array<int>)

# 팀장: "score 과목별로 저장하고 싶은데?"
# 나 : "아.. 네.. (미리 좀 말해줘요)"


class BySubjectGradeBook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}  # 여기 바뀜 [] => {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

book = BySubjectGradeBook()
book.add_student('Albert')
book.report_grade('Albert', 'Math', 75)
book.report_grade('Albert', 'Math', 85)
book.report_grade('Albert', 'Gym', 30)
book.report_grade('Albert', 'Gym', 25)

# BySubjectGradeBook <>- 1..1 -- grades: dict
# grades(name: key, score_by_subject: dict)
# score_by_subject(subject: key, score: int)

# 나: "대충 테스트해보니 잘 되네. 리뷰 받아야지."
# 팀장: "아니, 이건 너무 단순한데, 쪽지시험보다 중간/기말고사 점수가 더 중요하게 평가되게 가중치를 줘야겠어"
# 나: "네... ㅂㄷㅂㄷㅂㄷ"


class WeightedGradeBook(object):
    # ...
    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                # ...
                subject_avg += score
                total_weight += weight
        return 0

# BySubjectGradeBook <>- 1..1 -- grades: dict
# grades(name: key, score_by_subject: dict)
# score_by_subject(subject: key, score: tuple(score, weight))


"""
모델링을 할 때는 코드가 얼마나 길어지냐, 클래스가 얼마나 생성되느냐가 중요하지 않다.
얼마나 읽기 편하냐의 기준은 비단 코드의 길이만 영향을 미치는 것이 아니다. (내생각)
"""
