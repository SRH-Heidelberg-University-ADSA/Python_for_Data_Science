class Bst:
    def __init__(self, value):
        self.value = value  # self.value
        self.right = None  # self.edges = []
        self.left = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = Bst(value)
            else:
                self.left.insert(value)

    def search(self, value):
        current = self
        found = False
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                found = True
                break
        return found

    def search_recursive(self, value):
        if value == self.value:
            return True
        if value < self.value:
            if self.left is None:
                return False
            self.left.search_recursive(value)


b = Bst(100)
b.search(97)
