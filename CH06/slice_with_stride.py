"""

6. 한 슬라이스에 start, end, stride 를 함께 쓰지 말자.
-> 모든 기능이 필요하다면, start, end / stride 를 나누어서 사용하자.

Slice: somelist[start:end:stride]

"""

# stride 사용 예제
print('stride 사용 예제')
a = [1, 2, 3, 4, 5, 6]
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)

# 문자를 역순으로 만들기
print('문자를 역순으로 만들기')
x = 'mongoose'
y = x[::-1]
print(y)

# 바이트나 아스키 문자에선 역순으로 변환하는 것이 가능하지만,
# 인코드된 유니코드 문자에는 적용되지 않는다. (2Bytes 이상 사용해서 망하는듯)
w = '안녕하세요'
x = w.encode('utf-8')
y = x[::-1]
# z = y.decode('utf-8')  # <- 예외 구문

print(a[-2:])  # s: 5이고, e: 6(포함) 이니 이 구문은 맞는데
print(a[::-2])
print(a[-2::-2])  # MEMO: 이건 왜 5, 3, 1이 나오나??

# a[-2::-2] 는 아래와 같이 풀린다
# 참고: https://bytes.com/topic/python/answers/719309-slice-negative-stride
b = a[-2::-1]
print(b)
c = b[::2]
print(c)

# 결론은 stride 음수로 쓰지 말고 ㄱ-,
# 모든 기능을 사용해야 한다면 여러줄로 나눠 쓰는 것이 좋다. (괴랄하네..)
