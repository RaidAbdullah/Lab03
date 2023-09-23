def rep(x):
    def decorator(func):
        def wrapper():
            for _ in range(x):
                func()
        return wrapper
    return decorator

x = int(input("Enter a number of repetitions: "))


@rep(x)
def hello():
    print('Hello')

hello()
