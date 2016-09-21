"""

10. range 보다는 enumerate 를 사용하자

"""

# 단순 element 순회
flavor_list = ['a', 'b', 'c', 'd']
for flavor in flavor_list:
    print('{0} is element of flavor_list'.format(flavor))

# range 를 이용한 리스트 순회 (index 포함)
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('{0}: {1}'.format(i, flavor))

# enumerate 를 이용한 리스트 순회 (index 포함)  # better way
for i, flavor in enumerate(flavor_list):
    print('{0}: {1}'.format(i, flavor))
