from BL.AVLTree import AVLTree
from BL.AVLNode import Node


class AVLTreeManager(object):
    def __init__(self):
        self.tree = AVLTree()
        self.cont = 0

    def addNode(self, num):

        """if self.cont is 0:
            self.tree.initRoot(num)
            self.cont = self.cont+1
        else:
            self.tree.insert(self.tree.root, num)
        #self.tree.printHelper(self.tree.root, "", True)"""

        self.tree.addToTree(num)




    def getInOrden(self):
        return self.tree.getInOrden()

    def getPreOrden(self):
        return self.tree.getPreOrden()

    def getPostOrden(self):
        return self.tree.getPostOrden()