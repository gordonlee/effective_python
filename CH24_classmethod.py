"""

24. 객체를 범용으로 생성하려면 @classmethod 다형성을 이용하자.

- @classmethod 다형성은 생성된 객체가 아니라 전체 클래스에 적용된다는 점만 빼면
InputData.read 에 사용한 인스턴스 메서드 다형성과 똑같다.
(내용을 대충 보면, 다형성에서 사용하는 static member function 같은 느낌이다.)

"""
import os
import tempfile
from threading import Thread


# 객체의 상속 예제 ( InputData <- PathInputData )
class InputData(object):
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        super.__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


# map-reduce 예제 (model)
class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


# 위 클래스들을 생성하는 방법 예제
def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]  # MEMO: Thread header? from threading import Thread
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


# 순차적으로 호출
def map_reduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)
"""
이렇게 되면 map_reduce() 안에서 호출되는 함수는 이미 범용성을 잃는다.
애초에 Worker, InputData 클래스를 상속하는 의미가 없음.
(왜냐면, 저 부분을 다른 클래스로 바꾸려면 해당 함수들을 고쳐야 하기 때문에)

아래 부터는 리펙터링 후 모습.
"""


class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):  # FIXME: what is cls ?
        raise NotImplementedError


class PathInputData(GenericInputData):
    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def map_reduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


with tempfile.TemporaryDirectory() as tmpdir:
    # write_test_files(tmpdir)
    config = {'data_dir': tmpdir}
    result = map_reduce(LineCountWorker, PathInputData, config)
"""
타입 자체를 호출부에서 넘기게 되므로, 따로 함수 안을 고칠 필요가 없다.
다만, map_reduce() 에 넘어가는 argument 의 타입 체크를 걸어주는 편이 좋겠다.
"""
# FIXME: classmethod 의 정의를 먼저 알아보기 ( 정말 static member function 인가? )
