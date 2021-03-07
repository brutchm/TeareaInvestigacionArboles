from BL.BlackRedTree import BlackRedTree


class BlackRedManager(object):
    def __init__(self):
        self.tree = BlackRedTree()

    def insert(self, num):
        self.tree.insert(num)

    def print(self):
        self.tree.print_tree()