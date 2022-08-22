def repeat(num):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            print(num)
            for _ in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

# @repeat(3)
def func1(name):
    print(name)

repeat(5)(func1)('Test Python')
