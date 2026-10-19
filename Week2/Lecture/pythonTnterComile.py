a = 1
print(a)
# print("srh)

import dis


def some_function():
    a = 1
    if a == 1:
        print("yes")


dis.dis(some_function)
