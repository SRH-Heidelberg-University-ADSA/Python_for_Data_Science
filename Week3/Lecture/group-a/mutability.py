s = "hello"  #   4567 datatype : size
print(id(s))
s = s + "world"
print(id(s))

lst = [1, 2, 3]
print(id(lst))
lst.append(4)
print(id(lst))


def modify(lst, num):
    lst.append(num)
    num = num + 1


d = [1, 2]
x = 3
modify(d, x)
print(d)
print(x)
