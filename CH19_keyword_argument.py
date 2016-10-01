"""

19. 키워드 인수로 선택적인 동작을 제공하자.

"""


# 위치를 이용한 함수 호출 (파라메터 순서에 따라)
def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6

# 아래 호출은 모두 위 함수를 호출하도록 한다.
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

# 위치 인수는 키워드 인수보다 앞에 위치 해야한다.
# remainder(number=20, 7)  # Error

# 각 인수는 한 번만 지정할 수 있다.
# remainder(20, 7, number=20)  # Error
"""
키워드 인수의 유연성은 세 가지 중요한 장점(이점)이 있다.
    1) 호출부에서 명확한 의미를 유추할 수 있다.
    2) 함수를 정의할 때 기본값을 설정할 수 있다.
    3) 기존 코드의 호출 방식을 유지하면서 파라메터를 확장할 수 있다.
"""


# 함수 정의 시, 기본값 설정
def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print('{0} kg per second'.format(flow))


# 위 함수에 기간값을 추가하면 아래와 같은 모양으로 추가할 수 있다.
def flow_rate_add_param(weight_diff, time_diff, period):
    return weight_diff / time_diff * period


# 이렇게 되면 호출부를 모두 바꿔줘야 하는데, 아래 함수처럼 변형시키면 기존 모양을 유지할 수 있다.
def flow_rate_add_default_param(weight_diff, time_diff, period=1):
    return weight_diff / time_diff * period

flow_per_second = flow_rate_add_default_param(weight_diff, time_diff)  # 기본값
print(flow_per_second)

flow_per_hour = flow_rate_add_default_param(weight_diff, time_diff, period=3600)  # custom 값
print(flow_per_hour)
"""
선택적인 인수(디폴트값이 있는 파라메터)를 위치로 넘길 수도 있지만,
그럴경우 대응하는 파라메터가 어떤것인지 명확하지 않아
혼동을 일으킬 수 있다.
가장 좋은 방법은 항상 키워드 이름으로 선택적인 인수를 지정하고,
위치 인수로는 아예 넘기지 않는 것이다.
"""