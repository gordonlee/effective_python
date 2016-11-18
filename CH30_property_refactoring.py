"""

30. 속성을 리팩토링하는 대신 @property 를 고려하자.

정리
    - 기존의 인스턴스 속성에 새 기능을 부여하려면 @property 를 사용하자.
    - @property 를 사용하여 점점 나은 데이터 모델로 발전시키자.
    - @property 를 너무 많이 사용한다면 클래스와 이를 호출하는 모든 곳을
      리펙토링하는 방안을 고려하자.

"""
from datetime import datetime, timedelta


class Bucket(object):
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        # self.quota = 0  # property 로 뺀 변수
        # 할당량 추적을 위한 변수들 추가
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return 'Bucket(quota={0}, max={1}, consumed={2})'\
            .format(self.quota, self.max_quota, self.quota_consumed)

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            # 새 기간의 할당량을 리셋함
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # 새 기간의 할당량을 채움
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            # 기간 동안 할당량을 소비함
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


def fill(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True

# bucket 에 100을 부었다.
bucket_instance = Bucket(60)
fill(bucket_instance, 100)
print(bucket_instance)

# bucket 에서 99를 뺐다.
if deduct(bucket_instance, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print(bucket_instance)

# bucket 에서 3을 빼려고 시도했다. (그러나 실패)
if deduct(bucket_instance, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
print(bucket_instance)

"""
기존 변수를 property 로 setter 처리해도 구현부는 바뀔 내용이 없다.
(책에선) 다른 언어에서와 마찬가지로 너무 남발하지 말자.
property method 를 계속 확장하고 있다면, 클래스 리펙터링을 고려해보자.
"""