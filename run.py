from db import client
from utils.class_bench import class_bech
from utils.func_bech import func_decorator
from view.my_class import Sleep
from view.my_function import sleep_one_sec


@func_decorator
def say_smth(smth: str):
    sleep_one_sec()
    print(smth)


@class_bech
class Object:
    x: int
    y: int
    z: int

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def move(self, x, y):
        Sleep.sleep_three_secs(Sleep)
        self.x += x
        self.y += y

    def jump(self, z):
        Sleep.sleep_two_secs(Sleep)
        self.z += z


if __name__ == '__main__':
    say_smth("Hi!")
    obj_1 = Object(0, 0, 0)
    obj_1.move(1, 1)
    obj_1.jump(2)
    benchmarks = client.benchmarks
    class_benchmark = benchmarks.class_functions_benchmark
    func_benchmark = benchmarks.functions_benchmark
    result = func_benchmark.find()
    result_1 = class_benchmark.find()
    print(result)
    print(result_1)
