def my_function(param1, param2=1):  # name, params
    print(param1)  # body
    print(param2)


my_function(1)  # call

lst = [1, 2, 3]
print(*lst)


def unlimited_pos_arg(*args):
    print(type(args))
    print(*args)


unlimited_pos_arg(1, 2, 3, 5, 6, 7, "srh")


def key_wd_func(param1, param2):
    print(param1)
    print(param2)


key_wd_func(1, param2=2)


def unlimited_kw_args(**kwargs):
    print(type(kwargs))
    print(*kwargs)


unlimited_kw_args(a=1, z=67, b="srh")


def a():
    print("a called")
    b()
    print("a ended")
    # return 1000


def b(param1):
    print("b called")
    print(param1)
    c()
    print("b ended")


def c():
    print("c called")
    print("c ended")


a(b(c()))
