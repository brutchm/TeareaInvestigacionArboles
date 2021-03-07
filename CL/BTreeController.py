from BL.BTree import BTree

class BTreeController(object):
    def __init__(self, order):
        self.btree = BTree(scala=order)

    def insert_in_btree(self, num):
        self.btree.insert(num)

    def find(self, num):
        return "Los valores son: " + str(self.btree.find(num).values) + " y los hijos son: " + str(self.btree.find(num).children)

    def delete(self, num):
        self.btree.delete(num)





