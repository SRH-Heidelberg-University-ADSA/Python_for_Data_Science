def my_function(param1, param2):
    print(param1)
    print(param2)


my_function(1, 2)


def my_function_any(*args):
    print(type(args))
    print(args)


# print(type(*args))


my_function_any(1, 2, 3, 4, 5, "srh")


def my_function_kw(param2, param1=None):
    print(param1)
    print(param2)


my_function_kw(param2="a")


def my_function_kw_any(**kwargs):
    print(type(kwargs))
    print(*kwargs)
    return kwargs


result = my_function_kw_any(a=1, b=2, c=3)
print(result)

x = 100


def c():
    print("c called")
    # print(x)
    value = x * 100
    print(value)
    # x = 101
    print("c ended")


def b():
    print("b called")
    c()
    print(" b ended")


def a():
    print("a called")
    b()
    print("a ended")


a()
print(x)
