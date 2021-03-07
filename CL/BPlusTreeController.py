from BL.BPlusTree import BPlusTree

class BPlusTreeController(object):
    def __init__(self, order):
        self.bplustree = BPlusTree(order=3)

    def insert_in_bplustree(self, num):
        self.bplustree.insert(num, num)
        return self.bplustree.show()

    def find(self, num):
        return str(self.bplustree.retrieve(num))


