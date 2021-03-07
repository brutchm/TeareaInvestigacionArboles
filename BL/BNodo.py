class BNodo(object):
    def __init__(self, scala=3):
        self.values = []
        self.parent = None
        self.children = []

    def insert(self, value):
        if value in self.values:
            pass
        else:
            self.values.append(value)
            self.values.sort()
        return len(self.values)

    def compare(self, value):
        length = len(self.values)
        if self.children == [] or value in self.values:
            return None

        for i in range(length):
            if value < self.values[i]:
                return i
        return i + 1

    def getPos(self):
        return self.parent.children.index(self)

    def getValLen(self):
        return len(self.values)






