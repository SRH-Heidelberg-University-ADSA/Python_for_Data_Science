# print("hello world")
# a = 123

f = open(
    "/Users/D068192/dev/codes/git/srh/python/python-foundation/Python_for_Data_Science/Week5/Lecture/group-b/notes.txt",
    mode="rb",
    # encoding="utf-8",
)

for line in f:
    if b"\n" in line:
        print(line)

contents = f.read()
# print(contents)


# with open() as f:
# generators
def my_generator():
    print("generator called")
    yield 1
    print("1 yielded")
    yield 2
    print("2 yielded")


# result = my_generator()
# first = result.__next__()
# print(first)
# result.__next__()
# result.__next__()

# with open() as f:
from contextlib import contextmanager


@contextmanager
def db_insert():
    print("create db conection")
    yield "con"
    print("connection closed")


# with db_insert() as c:
#    print(c)
#    print("inside the context")

# print("outside the context")
#
import csv

with open(
    "/Users/D068192/dev/codes/git/srh/python/python-foundation/Python_for_Data_Science/Week5/Lecture/group-b/people.csv"
) as f:
    content = csv.DictReader(f)
    for row in content:
        print(row)

import json

with open(
    "/Users/D068192/dev/codes/git/srh/python/python-foundation/Python_for_Data_Science/Week5/Lecture/group-b/people.json"
) as f:
    content = json.load(f)
    print(content)

try:
    with open("") as f:
        print("file opened")
except FileNotFoundError:
    print("file not found")
except ValueError:
    print("value rror")
except Exception as e:

#except 
    
#else:

