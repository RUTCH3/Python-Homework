import time


def my_decorator(n):
    def wrapper(func):
        def inner(*args):
            print("in decorator")
            start_time = time.time()
            print(start_time)
            func(*args, n)
            time2 = time.time()
            print(time2, time.time() - start_time)

        return inner

    return wrapper


@my_decorator(500)
def double(n):
    for i in range(n * n):
        print(i)
    print(n * n)


double()


def func_decorator():
    def wrapper(func):
        def inner(*args):
            pass

        return inner

    return wrapper
