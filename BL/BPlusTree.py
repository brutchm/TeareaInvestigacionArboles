from BL.BPlusNode import BPlusNode


class BPlusTree(object):
    """B+ tree object, consisting of nodes.
    Nodes will automatically be split into two once it is full. When a split occurs, a key will
    'float' upwards and be inserted into the parent node to act as a pivot.
    Attributes:
        order (int): The maximum number of keys each node can hold.
    """
    def __init__(self, order=8):
        self.root = BPlusNode(order)

    def _find(self, node, key):
        """ For a given node and key, returns the index where the key should be inserted and the
        list of values at that index."""
        for i, item in enumerate(node.keys):
            if key < item:
                return node.values[i], i

        return node.values[i + 1], i + 1

    def _merge(self, parent, child, index):
        """For a parent and child node, extract a pivot from the child to be inserted into the keys
        of the parent. Insert the values from the child into the values of the parent.
        """
        parent.values.pop(index)
        pivot = child.keys[0]

        for i, item in enumerate(parent.keys):
            if pivot < item:
                parent.keys = parent.keys[:i] + [pivot] + parent.keys[i:]
                parent.values = parent.values[:i] + child.values + parent.values[i:]
                break

            elif i + 1 == len(parent.keys):
                parent.keys += [pivot]
                parent.values += child.values
                break

    def insert(self, key, value):
        """Inserts a key-value pair after traversing to a leaf node. If the leaf node is full, split
        the leaf node into two.
        """
        parent = None
        child = self.root

        # Traverse tree until leaf node is reached.
        while not child.leaf:
            parent = child
            child, index = self._find(child, key)

        child.add(key, value)

        # If the leaf node is full, split the leaf node into two.
        if child.is_full():
            child.split()

            # Once a leaf node is split, it consists of a internal node and two leaf nodes. These
            # need to be re-inserted back into the tree.
            if parent and not parent.is_full():
                self._merge(parent, child, index)

    def retrieve(self, key):
        """Returns a value for a given key, and None if the key does not exist."""
        child = self.root

        while not child.leaf:
            child, index = self._find(child, key)

        for i, item in enumerate(child.keys):
            if key == item:
                return child.values[i]

        return None

    def show(self):
        """Prints the keys at each level."""
        self.root.show()
