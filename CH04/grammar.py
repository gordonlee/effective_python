"""

print() 함수에서 이해가 잘 안가던 부분인
"프린트안에서 쓰는 %r은 뭐고 % 이건 뭔가?"
이 부분에 대한 리서칭을 해본다.

formatting: https://pyformat.info/

* 참고> Quick Preview of Built-in Type
from (https://docs.python.org/3/library/stdtypes.html)
    Boolean Operations - and, or, not
    Numeric Types - int, float, complex
    Sequence Types - list, tuple, range
    Text Sequence Type - str
    Binary Sequence Types - bytes, bytearray, memoryview
    Set Types - set, frozenset
    Mapping Types - dict

"""

# Basic formatting
# Old style
print('=== Old Style ===')
print('%s %s' % ('one', 'two'))
print('%d %d' % (1, 2))

"""
old 스타일은 타입을 신경써서 %s, %d를 붙여야 한다.
이를 string.format() 을 이용해서 묶어 버리면
타입에 대해 크게 신경쓰지 않아도 된다.
"""

# New style
print('=== New Style ===')
print('{} {}'.format('one', 'two'))
print('{} {}'.format(1, 2))
print('--- OR (like C#) ---')
print('{1} {0}'.format('one', 'two'))
print('{1} {0}'.format(1, 2))
