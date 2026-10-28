class Bst:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self,value):
        if value < self.value:
            if self.left == None:
                self.left = Bst(value)
            else:
                self.left.insert(value)

        if value > self.value:


    def search(self,value):
        current = self
        found = False
        if current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                found = True
                break

            return found

        

b = Bst(100)
b.insert(99)
b.insert(98)

b.search(99)
