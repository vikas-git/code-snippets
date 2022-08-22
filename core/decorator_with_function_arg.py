# decorator with function argument
def decorator_func(func):
    def inner_1(*args, **kwargs):
        print("call decorator body before")
        func(*args, **kwargs)
        print("call decorator body after")
    return inner_1


@decorator_func
def call_param_function(n):
    print("call function body", n)
    return

#decorator_func(call_param_function)(10)
call_param_function(10)