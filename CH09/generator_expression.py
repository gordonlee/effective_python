"""

9. comprehension 이 클 때는 generator expression 을 고려하자

* comprehension 의 단점은 새 리스트를 통째로 생성한다는 점이다.
입력이 적을 때는 쓰고 버리면 되지만, 입력이 큰 경우는 메모리를 고갈 시킬 수 있다.
이런 경우에 사용할 수 있는 것이 generator expression 이다.

"""

# list comprehension 을 이용한 접근
value = [len(x) for x in open('my_file.txt', encoding='utf-8')]
print(value)

# generator expression 을 이용한 접근
it = (len(x) for x in open('my_file.txt', encoding='utf-8'))
print(it)
print(next(it))
print(next(it))
print(next(it))
"""
필요할 때, 내장함수인 next()로 iterator 를 전진시키면,
메모리를 한꺼번에 로딩하지 않고 단계별로 로딩한다.
"""

# 다른 제너레이터 표현식과 함께 사용할 수도 있다.
roots = ((x, x**0.5) for x in it)
print(next(roots))
