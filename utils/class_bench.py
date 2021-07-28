from db import client
import time
import inspect


def get_module_name(func):
    return inspect.getmodule(func)


def func_decorator(func, cls):
    def wrapper(*args, **kwargs):
        print(args)
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        benchmarks = client.benchmarks
        class_func_benchmark = benchmarks.class_functions_benchmark
        class_func_benchmark_data = {"class_name": cls.__name__,
                                     "module": get_module_name(func).__name__,
                                     "function": func.__name__,
                                     "args": args[1:],
                                     "kwargs": kwargs,
                                     "start_time": start_time,
                                     "end_time": end_time,
                                     "duration": end_time - start_time}
        class_func_benchmark.insert_one(class_func_benchmark_data)
    return wrapper


def class_bech(cls):
    functions = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for name, func in functions.items():
        func_name = str(func.__name__)
        if func_name.startswith('__'):
            continue
        else:
            dec_func = func_decorator(func, cls)
            setattr(cls, name, dec_func)
    return cls






