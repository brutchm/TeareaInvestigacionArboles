from BL.AVLNode import Node


class AVLTree(object):

    def __init__(self):
        self.root = None

    def initRoot(self, num):
        if self.root is None:
            root = Node(num)
            self.root = root

    def addToTree(self, num):

        self.root = self.insert(self.root, num)

    def insert(self, root, num):

        if root is None:
            return Node(num)
        elif root.info > num:
            root.left = self.insert(root.left, num)
        else:
            root.right = self.insert(root.right, num)

        return self.rebalance(root)

    def leftRotate(self, y):
        x = y.right
        z = x.left
        x.left = y
        y.right = z

        self.updateHeight(y)
        self.updateHeight(x)

        return x

    def rightRotate(self, y):
        x = y.left
        z = x.right
        x.right = y
        y.left = z

        self.updateHeight(y)
        self.updateHeight(x)

        return x

    def updateHeight(self, root):
        root.height = 1 + max(self.getHeight(root.right), self.getHeight(root.left))


    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    def getBalance(self, root):
        if root is None:
            return 0
        return self.getHeight(root.right) - self.getHeight(root.left)

    def rebalance(self, root):
        self.updateHeight(root)
        balance = self.getBalance(root)

        if balance > 1:
            if self.getHeight(root.right.right) > self.getHeight(root.right.left):
                root = self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                root = self.leftRotate(root)
        elif balance < -1:
            if self.getHeight(root.left.left) > self.getHeight(root.left.right):
                root = self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                root = self.rightRotate(root)

        return root


    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)


    def inOrdenRecursive(self, root):
        if not root:
            return ""
        else:
            return self.inOrdenRecursive(root.left) + str(root.info) + "," + self.inOrdenRecursive(root.right)

    def preOrdenRecursive(self, root):
        if not root:
            return ""
        else:
            return str(root.info) + "," + self.preOrdenRecursive(root.left) + self.preOrdenRecursive(root.right)

    def postOrdenRecursive(self, root):
        if not root:
            return ""
        else:
            return self.postOrdenRecursive(root.left) + self.postOrdenRecursive(root.right) + str(root.info) + ","

    def getInOrden(self):
        return self.inOrdenRecursive(self.root)

    def getPreOrden(self):
        return self.preOrdenRecursive(self.root)

    def getPostOrden(self):
        return self.postOrdenRecursive(self.root)

    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            print(indent)
            if last:
                print("R----")
                indent += "     "
            else:
                print("L----")
                indent += "|    "
            print(currPtr.info)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

