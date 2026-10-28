s = "hello"
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


l = [1, 2, 3]
n = 4
modify(l, n)
print(l)
print(n)
