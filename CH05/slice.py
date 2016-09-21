"""

** Sequence Slice **

대상:
    내장타입: list, str, bytes
    커스텀타입: __getitem__ , __setitem__ 메서드가 구현되어 있는 클래스

* 팁1.
파이썬 메모리 구조를 살펴보고 싶다면,
http://www.pythontutor.com/ 에서 볼 수 있다.
* 팁2.
파이썬의 List Comparison
https://docs.python.org/2/tutorial/datastructures.html#comparing-sequences-and-other-types

"""

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Origin: {0}'.format(a))

# 기본 활용
print('a[:]: {0}'.format(a[:]))
print('a[5:]: {0}'.format(a[5:]))
print('a[-3:-1]: {0}'.format(a[-3:-1]))

# 치환하기
print('replace before : {0}'.format(a))
a[2:7] = [99, 23, 124]
print('replace after: {0}'.format(a))

# 슬라이스에서 시작과 끝 인덱스를 지정하지 않고 할당하면,
# (새 리스트를 할당하지 않고) 슬라이스의 전체 내용을
# 참조 대상의 복사본으로 대체한다.
b = a
print('AllocTest Before: {0}'.format(a))
a[:] = [101, 32, 142]
assert a is b
print("AllocTest After : {0}".format(a))

# 정상값으로 성공, a[:5] 와 a[0:5]가 동일한 리스트를 참조하고 있는 형태가 아니라,
# 서로 다른 메모리 공간을 갖고 있지만, == 연산자가 T를 반환
# https://docs.python.org/2/tutorial/datastructures.html#comparing-sequences-and-other-types
b = a[:5]
c = a[0:5]

b.append('qq')
c.append('qq')

# 아마 리스트에 메모리 공간이 아니라, 모든 값들이 같은지를 체크하는 듯
if b == c:
    print("== t")
else:
    print('== f')

# 동일한 리스트를 가르키고 있는지 체크하는 듯
if b is c:
    print('b is c')
else:
    print('b is not c')

