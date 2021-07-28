import db
import time
import inspect


def get_module_name(func):
    return inspect.getmodule(func)


def func_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        benchmarks = db.client.benchmarks
        func_benchmark = benchmarks.funcions_benchmark
        func_benchmark_data = {"module": get_module_name(func).__name__,
                               "function": func.__name__,
                               "args": args,
                               "kwargs": kwargs,
                               "start_time": start_time,
                               "end_time": end_time,
                               "duration": end_time - start_time}
        func_benchmark.insert_one(func_benchmark_data)
    return wrapper


