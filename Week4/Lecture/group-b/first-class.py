# first class citizen
#
# Rule 1 : the citizen should be assignable to a variable
s = "srh"


# rule 2: the citizen must be passable into a functiomn
def my_func(param):
    print(param)


my_func("srh")


# rule 3: the citizen must be returnable from a function
def my_func_1():
    return "srh"


# result = my_func_1()
print(my_func_1())


def r1_func():
    print("r1 func")
    # return "srh"


x = r1_func
x()


def passed_function():
    print("passed function")


def calling_function(param1):
    param1()


calling_function(passed_function)


def outer_function():

    def inner_function():
        print("inner function")

    return inner_function


# result = outer_function()
print(outer_function())

print(dir(outer_function))

x = 1
# x()
import time


def timer(func):
    def inner_function(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f" { func.__name__}  took {end - start} seconds")

    return inner_function


@timer  # reult = timer(file_reader )   -> result ()
def file_reader():
    print("reading file")


@timer
def insert_into_db(query):
    print("insert db called")


file_reader()
insert_into_db("insert into db value")
