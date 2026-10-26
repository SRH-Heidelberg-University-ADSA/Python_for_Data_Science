a = [1, 2, 3]

# for z in a:
#    print(z)

my_iterator = iter(a)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# print(next(my_iterator))

b = 1
# my_iterator = iter(b)
# for z in b:
#    print(b)


class MyIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        value = self.current

        self.current = self.current - 2
        return value


a = MyIterator(10)
for z in a:
    print(z)
