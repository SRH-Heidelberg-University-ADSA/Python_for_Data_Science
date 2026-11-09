# for i in range(1, 100):
import csv
import json

with open(
    "/Users/D068192/dev/codes/git/srh/python/python-foundation/Python_for_Data_Science/Week5/Lecture/group-a/people.json",
    "r",
    encoding="utf-8",
    newline="",
) as f:
    data = json.load(f)
    print(data)
    s = '{"age":30, "name":"doe }'
    json.dumps(s)

    # reader = csv.DictReader(f)
    # for row in reader:
    #    print(row)
    # for line in f:
    #    if b"\n" in line:
    #        print("new line character found")

    # print(content)


# generators function
def my_generator():
    print("generator called")
    yield 1
    print("1 yielded")
    yield 2
    print("2 yielded")
    yield 3
    print("3 yielded")


result = my_generator()
# ia = result.__next__()
# print(a)
# result.__next__()
# result.__next__()
# result.__next__()
# with  open() as f:
#
#
from contextlib import contextmanager


@contextmanager
def my_func():
    print("my_func called")
    yield 1
    print("automatically called")


# with my_func() as a:
#    print(a)
#    print("inside my context")

# print("outside")i
try:
    with open("something.txt") as f:
        file = f.read()
except FileNotFoundError:
    print("file does not exist")
except ValueError:
    print("file content is not correct")
except Exception as e:
    print(f"unhandelled {e} ")

try:

except
else:
finally:

