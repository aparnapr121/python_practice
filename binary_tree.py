class BSTNode(object):
    def __init__(self, parent, k):
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None


    def insert(self, node):
        """
        insert a node into the subtree rooted at this node
        """
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node 
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def find(self, k):
        """
        Finds and returns the node with key k from the subtree rooted at this
        """
        if k == self.key:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)

    def find_min(self):
        """
        Find the node with the minimum key at the subtree rooted at this node
        """
        if self.left is None:
            return self:
        else:
            return self.left.find_min()

    def next_larger(self):
        """
        Returns the node with the next larger key than the current node
        """
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent


    def delete(self):
        """
        Deletes and returns this node from BST
        """
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right. = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()
            
        