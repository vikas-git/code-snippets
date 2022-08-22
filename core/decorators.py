# simple decorator without argument
def decorator_func(func):
    def inner():
        print("call decorator body before")
        func()
        print("call decorator body after")
    return inner

# 1st way
@decorator_func
def call_function():
    print("call function body")
    return

call_function()

# 2nd way
def call_function():
    print("call function body")
    return

# or we can call function like
decorator_func(call_function)()
