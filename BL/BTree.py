from BL.BNodo import BNodo
import sys
import math

class BTree(object):


    def __init__(self, node: BNodo = None, scala=3):
        self.root = BNodo(scala=scala)
        self.scala = scala
        self.mid_index = int((self.scala - 1) / 2)

    def _find(self, value, node: BNodo = None):
        if not node:
            return BTree.compare(value, self.root)
        else:
            return BTree.compare(value, node)

    def find(self, value, node: BNodo = None):
        if not node:
            _node = self.root
        else:
            _node = node

        result = _node.compare(value)
        if result is None:
            return _node
        else:
            return self.find(value, node=_node.children[result])

    def _split(self, node):
        if len(node.values) <= self.scala - 1:
            return 0

        parent = node.parent
        new_node, l_node, r_node = BNodo(), BNodo(), BNodo()

        mid_index = self.mid_index
        l_node.values = node.values[0:mid_index]
        center = node.values[mid_index]
        r_node.values = node.values[mid_index + 1:]

        if node.children != []:
            l_node.children = node.children[0:mid_index + 1]
            r_node.children = node.children[mid_index + 1:]
            for i in range(mid_index + 1):
                node.children[i].parent = l_node
            for i in range(mid_index + 1, self.scala + 1):
                node.children[i].parent = r_node

        if not parent:
            parent = new_node
            parent.values.append(center)
            parent.children.insert(0, l_node)
            parent.children.insert(1, r_node)
            l_node.parent = parent
            r_node.parent = parent
            self.root = parent
            return 0

        l_node.parent = parent
        r_node.parent = parent
        parent.insert(center)
        index = parent.children.index(node)
        parent.children.pop(index)
        parent.children.insert(index, l_node)
        parent.children.insert(index + 1, r_node)
        return self._split(parent)

    def stepCover(self, node: BNodo, value_pos):  # value_pos indicates the position of the deleted value
        if node.children == []:
            return self.merge(node, node.getPos())

        after = node.children[value_pos + 1]
        node.insert(after.values.pop(0))
        return self.stepCover(after, 0)

    def merge(self, node, pos):
        if not node.parent:
            return 0

        if node.getValLen() >= self.mid_index:
            return 0

        parent = node.parent
        if pos:
            pre = parent.values[pos - 1]
            bnode = parent.children[pos - 1]
        else:
            pre = None
            bnode = parent.children[1]

        if bnode.getValLen() > self.mid_index:
            return self.rotate(node, bnode, parent, pre)

        if not pre:
            node.insert(parent.values.pop(0))
            bnode.children = node.children + bnode.children
        else:
            node.insert(parent.values.pop(pos - 1))
            bnode.children = bnode.children + node.children
        bnode.values += node.values
        bnode.values.sort()
        parent.children.remove(node)
        if parent.getValLen() == 0 and not parent.parent:
            self.root = bnode
            return 0

        if parent.getValLen() < self.mid_index:
            return self.merge(parent, parent.getPos())

    def rotate(self, node, bnode, parent, pre):
        if not pre:
            return self.leftRotate(node, bnode, parent)
        return self.rightRotate(node, bnode, parent)

    def leftRotate(self, node, bnode, parent):
        node.insert(parent.values.pop(0))
        parent.insert(bnode.values.pop(0))
        return 0

    def rightRotate(self, node, bnode, parent):
        pos = node.getPos()
        node.insert(parent.values.pop(pos - 1))
        parent.insert(bnode.values.pop(-1))
        return 0

    def insert(self, *values):
        for value in values:
            node = self.find(value)
            length = node.insert(value)
            if length == self.scala:
                self._split(node)

    def delete(self, value):
        node = self.find(value)
        value_pos = node.values.index(value)
        node.values.remove(value)
        self.stepCover(node, value_pos)



