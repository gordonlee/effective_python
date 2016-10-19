"""

26. 믹스인 유틸리티 클래스에만 다중 상속을 사용하자.

> 믹스인(mix-in) ?
클래스에서 제공해야 하는 추가적인 메서드만 정의하는 작은 클래스.

요약:
    믹스인 클래스로 같은 결과를 얻을 수 있다면 다중 상속을 사용하지 말자.
    인스턴스 수준에서 동작을 고체할 수 있게 만들어진
    믹스인 클래스가 요구할 때 클래스 별로 원하는 동작을 설게하자.
    간단한 동작들로 복잡한 기능을 생성하려면 믹스인을 조합하자.

"""
import json


class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left, right)
        self.parent = parent

    def _traverse(self, key, value):  # 오버라이드
        if isinstance(value, BinaryTreeWithParent) and key == 'parent':
            return value.value  # 순환 방지
        else:
            return super()._traverse(key, value)


tree = BinaryTree(
    10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11)))
print(tree.to_dict())

root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
print(root.to_dict())  # FIXME: 흠 이게 순환참조가 되는 구조인가?


class NamedSubTree(ToDictMixin):
    def __init__(self, name, tree_with_parent):
        self.name = name
        self.tree_with_parent = tree_with_parent

my_tree = NamedSubTree('foobar', root.left.right)
print(my_tree.to_dict())


class JsonMixin(object):

    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict())


class DataCenterRack(ToDictMixin, JsonMixin):
    def __init__(self, switch=None, machines=None):
        self.switch = Switch(**switch)
        self.machines = [Machine(**kwargs) for kwargs in machines]


class Switch(ToDictMixin, JsonMixin):
    def __init__(self, ports, speed):
        self.ports = ports
        self.speed = speed


class Machine(ToDictMixin, JsonMixin):
    def __init__(self, cores, ram, disk):
        self.cores = cores
        self.ram = ram
        self.disk = disk


serialized = """{
"switch": {"ports": 5, "speed": 1e9},
"machines":[
    {"cores":8, "ram": 32e9, "disk": 5e12},
    {"cores":4, "ram": 16e9, "disk": 1e12},
    {"cores":2, "ram": 4e9, "disk": 500e9}
]
}"""

deserialized = DataCenterRack.from_json(serialized)
round_trip = deserialized.to_json()
assert json.loads(serialized) == json.loads(round_trip)
