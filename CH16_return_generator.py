from itertools import islice

"""

16. 리스트를 반환하는 대신 제너레이터를 고려하자.

"""


# 리스트를 리턴하는 함수 코드 예제
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result

address = 'Four score and seven years ago...'
output = index_words(address)
print(output[:3])
"""
위 예제에 대해 두 가지에 대해 생각해 볼 수 있다.
    1) 코드가 깔끔하지 않다.
        : 함수가 길고, 무엇을 저장하는지 한번에 파악이 어렵다.
    2) 반환하기 전에 모든 정보들을 우선 리스트에 담아야 한다.
        : 메모리가 한정되어 있거나, input 자체가 큰 경우는 문제상황이 생길 수 있다.
"""


# generator 로 풀어낸 동일 함수 로직
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

alloc_output_list = list(index_words_iter(address))
print(alloc_output_list[:3])


# file 에서 한 줄씩 읽어서 한 번에 한 단어씩 출력을 내어주는 함수
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

with open('./_data/address.txt', 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 3)
    print(list(results))


# 이건 내가 따로 작성한 버전 ( offset 변수 굳이 필요한걸까? )
def index_file_iter(handle):
    for line in handle:
        if line:
            yield 0
        for index, letter in enumerate(line):
            if letter == ' ':
                yield index + 1

with open('./_data/address.txt', 'r') as f:
    it = index_file_iter(f)
    results = islice(it, 0, 3)
    print(list(results))
