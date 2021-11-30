def log_decorator(func):
    def wrap():
        print(f'Calling func {func}')
        func()
        print(f'Func {func} finished it\'s work')
    return wrap

def hello():
    print('hello world')

wrapped_by_logger = log_decorator(hello)
wrapped_by_logger()

@log_decorator
def hello():
    print('hello, world')

hello()

from timeit import default_timer as timer
import math
import time

def measure_time(func):
    def inner(*args, **kwargs):
        start = timer()
        func(*args,*kwargs)
        end = timer()

        print(f'Function {func.__name__} took {end-start} for execution')

    return inner

@measure_time
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))

factorial(100)
