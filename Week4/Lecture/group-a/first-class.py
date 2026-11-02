# entity : first class citizen

# Rule 1: entity must be assignable to a variable
x = "srh"


# Rule 2: entity must be passable into a function
def rule_2(param):
    print(param)


rule_2("srh")


# rule 3: the entity should returned from a function
def rule_3(param):
    return param


result = rule_3("srh")
print(result)


# If function a first class citizen in python
def f_rule_1():
    print(" f rule 1 called")


x = f_rule_1
x()


def f_rule_3():
    print("f 2 called")

    def inner_function():
        print("inner function called")
        return 1

    return inner_function


result = f_rule_3()
result()


def f_rule_2(param):
    param()


def passed_function():
    print("passed function called")


f_rule_2(passed_function)

print(dir(passed_function))


def calculate_discount(price):
    return price * 0.50


# discount = calculate_price(500)
# discount = lambda price: price * 0.50  # a = lambda(price) return price *0.50


# Decorators
#
#
import time


def timer(func):
    def inner_function(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{ func.__name__  } took {end -start} seconds ")

    return 1


@timer  # result = timer(file_reader)   --> result()
def file_reader():
    print("reading files")


@timer
def insert_db(conn, query):
    print("insert into db")


file_reader()
insert_db("conn", "query")
