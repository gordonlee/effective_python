"""

12. for 와 while 루프 뒤에는 else 블록을 쓰지 말자

* 파이썬만의 새로운 문법인데, 루프 뒤에 else 블록을 걸 수 있단다.
근데, 이게 오묘하게 동작해서 오히려 오해의 소지가 높다.
(있는지도 몰랐다 ㄱ-)

"""


def coprime(lhs, rhs):
    for i in range(2, min(lhs, rhs) + 1):
        if lhs % i == 0 and rhs % i == 0:
            return False
    return True

# loop-else 예제
# 루프가 '완료'되면 들어오는 블록이다.
print('loop-else 예제')
for i in range(3):
    print('index: {0}'.format(i))
else:
    print('else block')

# loop-break 예제
# else 는 루프가 '완료'되지 않고, 중간에 빠져나가면(break) 호출되지 않는다.
# (뭐 이래........)
print('loop-break 예제')
for i in range(3):
    print('index: {0}'.format(i))
    if i == 1:
        break
else:
    print('else block')  # 안불림.. 위에서 break 걸려서 빠져나옴

# 빈 루프에서의 loop-else 예제
print('빈 루프에서의 loop-else 예제')
for x in []:
    print('Empty')
else:
    print('for else block')

while False:
    print('Empty')
else:
    print('while else block')

"""
서로소(coprime: 공양수가 1밖에 없는 둘 이상의 수)를 판별할 때 사용할 수 있긴
하지만, 가독성 상 원래 다른 언어에서 사용하는 방식을 따라가는 것이 나아보인다.
"""
a = 10
b = 20
# loop-else 문 없이 사용하는 방법 (1)
print('loop-else 문 없이 사용하는 방법 (1)')
print(coprime(a, b))

# loop-else 문 없이 사용하는 방법 (2)
print('loop-else 문 없이 사용하는 방법 (2)')
is_coprime = True
for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        is_coprime = False
        break
print(is_coprime)
