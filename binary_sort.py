class BSTNode:
    def __init__(self,parent,k):
        self.key=k
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, k):
        """find a node with the key k in the tree rooted at this node"""
        if self.key == k:
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
        """Find a node with the minimum key in the subtree rooted at this noe"""
        node=self
        while node.left is not None:
            node = node.left
        return node

    def next_larger(self):
        """Returns the node with the next largest key in the BST"""
        if self.right is not None:
            return self.right.find_min()
        else:
            current = self
            while current.parent is not None and current is current.parent.right:
                current = current.parent
            return current.parent

    def delete(self):
        """Delete and returns this node from the BST"""
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.right or self.left
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s=self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()

    def insert(self,node):
        if node is None:
            return None
        else:
            if self.key > node.key:
                    if self.left is None:
                        self.left=node
                        node.parent=self
                    else:
                        self.left.insert(node)
            else:
                if self.right is None:
                    self.right = node
                    node.parent = self
                else:
                    self.right.insert(node)

    def __str__(self):
        if self.key is not None:
            return f"(key={self.key})"
        else:
            return("key is None")

class BST:
    def __init__(self):
        self.root = None

    def find(self, k):
        return self.root and self.root.find(k)

    def find_min(self):
        return self.root and self.root.find_min()


    def insert(self,k):
        node = BSTNode(None,k)

        if self.root is None:
            self.root = node
            #print(self.root)
        else:
            self.root.insert(node)

    def delete(self,k):
        node=self.find(k)
        if node is self.root:
            pseudo_root = BSTNode(None,0)
            pseudo_root.left=node
            node.parent=pseudo_root
            del_node = node.delete()
            self.root = pseudo_root.left
            if self.root is not None:
                self.root.parent = None
            return del_node
        else:
            return node.delete()




    def print_tree(self):
        node=self.root
        self.print_nodes(node)

    def print_nodes(self,node,level=1):
        #print(node)
        #print("here")
        if node:
            #print("here 1")
            #print(node.left)
            self.print_nodes(node.left)
            print(node)
            #print("here 2")
            #print(node.right)
            self.print_nodes(node.right)

    def next_larger(self,k):
        node = self.find(k)
        return node and node.next_larger()


obj=BST()
obj.insert(10)
obj.insert(5)
obj.insert(20)

obj.insert(19)

#obj.insert(25)
#obj.insert(8)

#obj.print_tree()
#print(obj.root)
print(obj.next_larger(19))
#print(obj.root)
#obj.print_tree()
