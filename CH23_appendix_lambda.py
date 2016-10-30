"""

lambda 에 대하여
http://www.secnetix.de/olli/Python/lambda_functions.hawk

"""


def make_incrementor(n):
    return lambda x: x - n

f = make_incrementor(2)  # lambda x: x - 2
print(f(42))  # x->42(argument)  => f(42) -> 42 - 2 => 40

print(make_incrementor(2)(42))  # 붙여서 사용하면 이런 모양


# 간단한 사용자 sort 예제
names = ['aaa', 'bbbb', 'cc', 'dddddddddd']
names.sort(key=lambda x: len(x))
print(names)

