"""

    ** List Comprehension(리스트 훔축 표현식) **

"""

# ----- 리스트에 모든 요소에 제곱수를 수행 -----
# list comprehension 을 이용해서 수행
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x ** 2 for x in a]
print(type(squares))  # list type
print(squares)

# map 을 사용해서 풀어낼 수도 있지만, 깔끔하지 않다(?)
squares = map(lambda x: x ** 2, a)
print(type(squares))  # map type
print(squares)

# ----- 짝수에만 제곱수 -----
# list comprehension 을 이용해서 수행
even_squares = [x ** 2 for x in a if x % 2 == 0]
print(type(even_squares))
print(even_squares)

# map 과 filter 를 사용해서 수행
alt = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)

# dict 와 set 도 comprehension 을 사용할 수 있다.
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
# key, value 는 일종의 별칭, 포인트는 순서인듯
rank_dict = {value: key for key, value in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}

print(chile_ranks)
print(rank_dict)
print(chile_len_set)

