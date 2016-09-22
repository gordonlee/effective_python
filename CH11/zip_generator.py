"""

11. 이터레이터를 병렬로 처리하려면 zip 을 사용하자

"""

names = ['aaaa', 'bbbbbb', 'cc']
letters = [len(n) for n in names]

# names 중 길이가 가장 긴 str 을 찾기
longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
print(longest_name)

# CH10 적용
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
print(longest_name)

# zip generator
# index 순회를 두 개 이상의 제너릭에다가 한다.
# names 는 name 으로, letters 는 count 로!
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)

"""
문제점
1) 파이썬2 에서는 zip 이 제너레이터가 아니다. 이터레이터를 완전히 순회해서
zip 으로 생성한 모든 튜플을 반환한다. 그래서 메모리를 걱정해야 한다면,
itertools 에 있는 izip 을 사용해야 한다.
2) 두 개 이상의 리스트를 묶어서 처리하는 방식인데,
길이가 다른 경우 삼켜버린다. (길이가 같다고 확신이 안되면,
itertools 의 zip_longest 를 사용하는걸 고려해보자. (근데 이건 너무 specific case)
"""

# 삼키는 케이스
print('-- error case --')
names.append('dddddd')
for name, count in zip(names, letters):
    print(name)
