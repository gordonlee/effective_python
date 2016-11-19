# namedtuple? https://pythontips.com/2015/06/06/why-should-you-use-namedtuple-instead-of-a-tuple/
"""
tuple 은 list 와 다르게 tuple 안에 있는 값을 변경할 수 없다!

With namedtuples you don’t have to use integer indexes for accessing members of a tuple
namedtutple 은 integer index 로 요소를 접근 할 수 없다.
마치 dict 처럼 이름으로 접근할 수 있다. 그런데 중간에 변경할 수 없다.
"""
man = ('aa', 3)
print(man[0])

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
# Animal = namedtuple('Animal', 'name age')  # Error!
# Animal = namedtuple('Animal', 'name age type new_variable')  # Error!

perry3 = Animal("perry", 31, "cat")
perry = Animal("perry", type=31, age="cat")
perry = Animal(name="perry", age=31, type="cat")
perry2 = Animal(name="perry", age="123123", type="cat")

print('------')
print(perry2)
print('------')
print(perry3)

print(perry)
# Output: Animal(name='perry', age=31, type='cat')

print(perry.name)# Output: 'perry'

# perry.name = 'gordonlee'  # Error!

print(perry[0])  # fine

print(perry._asdict())
