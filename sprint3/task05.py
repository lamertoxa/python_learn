def logger(f):
    def wrapper(*arg, **kwargs):
        if f.__name__ == "print_arg":
            res = f(*arg, **kwargs)
            print(
                f"Executing of function {f.__name__} with arguments {', '.join([str(i) for i in list(arg) + list(kwargs.values())])}...")
            return res
        print(
            f"Executing of function {f.__name__} with arguments {', '.join([str(i) for i in list(arg) + list(kwargs.values())])}...")
        return f(*arg, **kwargs)

    return wrapper


@logger
def concat(*args, **kwargs):
    concated = ""
    for item in list(args) + list(kwargs.values()):
        concated = concated + str(item)
    return concated


@logger
def sum(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)