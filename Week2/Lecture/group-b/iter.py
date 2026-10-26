apartments = "srh"

# for apartment in apartments:
#    print(apartment)
my_iterator = iter(apartments)

print(my_iterator.__next__())
print(my_iterator.__next__())
print(my_iterator.__next__())
# print(my_iterator.__next__())


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
for each in a:
    print(each)
