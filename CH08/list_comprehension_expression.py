"""

8장. list comprehension 에서 표현식을 두 개 이상 쓰지 말자

flat = [x for row in matrix for x in row] 의 경우
flat = [x { for row in matrix } for x in row] 로 1차원 배열로 끊어서 보고
각 row 를 다시 반복하는 부분이 뒤에 있는 for x in row 로 이해하면 된다.

"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 이중 for 문도 아래와 같이 돌릴 수 있다.
"""
flat = [x for row in matrix for x in row] 의 경우
flat = [x { for row in matrix } for x in row] 로 1차원 배열로 끊어서 보고
각 row 를 다시 반복하는 부분이 뒤에 있는 for x in row 로 이해하면 된다.
"""
flat = [x for row in matrix for x in row]
print(flat)

# 풀어쓰면 아래와 같이 풀어서 쓸 수도 있다.
flat2 = []
for x in matrix:
    for elem in x:
        flat2.append(elem)
print(flat2)

# 각 요소에 대한 제곱수를 처리해보자
squared = [[x ** 2 for x in row] for row in matrix]
print(squared)

"""
위 내용 까지는 쉽게 이해할 수 있지만, 3중 포문이나 2중 포문도 조건이 복잡해지면,
코드를 읽는 사람이 따라가기가 어렵다.
그럴 땐, 풀어서 써주는 것이 가독성 상에선 더 좋다.
"""

# list comprehension 에서 다중 if 문
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]
assert b == c

# matrix 인스턴스에서 row 의 합이 10 이상이고, 3으로 나누어 떨어지는
# 셀을 구한다고 한다면?
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(filtered)
"""
내용이 복잡해 질 수록 직관적으로 이해하기가 어려워진다.
이럴 경우는 차라리 풀어서 써주는 것이 읽는 사람 입장에선 편하다.
"""
