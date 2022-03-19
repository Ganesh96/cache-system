class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None: #x is root
            self.root = y

        elif x == x.parent.left: #x is left child
            x.parent.left = y

        else: #x is right child
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None: #x is root
            self.root = y

        elif x == x.parent.right: #x is right child
            x.parent.right = y

        else: #x is left child
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, n):
        while n.parent != None: #node is not root
            if n.parent == self.root: #node is child of root, one rotation
                if n == n.parent.left:
                    self.right_rotate(n.parent)
                else:
                    self.left_rotate(n.parent)

            else:
                p = n.parent
                g = p.parent #grandparent

                if n.parent.left == n and p.parent.left == p: #both are left children
                    self.right_rotate(g)
                    self.right_rotate(p)

                elif n.parent.right == n and p.parent.right == p: #both are right children
                    self.left_rotate(g)
                    self.left_rotate(p)

                elif n.parent.right == n and p.parent.left == p:
                    self.left_rotate(p)
                    self.right_rotate(g)

                elif n.parent.left == n and p.parent.right == p:
                    self.right_rotate(p)
                    self.left_rotate(g)

    def insert(self, n):
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        n.parent = y

        if y == None: #newly added node is root
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n

        self.splay(n)

    def search(self, n, x):
        if x == n.data:
            self.splay(n)
            return n

        elif x < n.data:
            return self.search(n.left, x)
        elif x > n.data:
            return self.search(n.right, x)
        else:
            return None

    def delete(self, n):
        self.splay(n)
        left_subtree = SplayTree()
        left_subtree.root = self.root.left
        if left_subtree.root != None:
            left_subtree.root.parent = None

        right_subtree = SplayTree()
        right_subtree.root = self.root.right
        if right_subtree.root != None:
            right_subtree.root.parent = None

        if left_subtree.root != None:
            m = left_subtree.maximum(left_subtree.root)
            left_subtree.splay(m)
            left_subtree.root.right = right_subtree.root
            self.root = left_subtree.root
        else:
            self.root = right_subtree.root

    def inorder(self, n):
        if n != None:
            self.inorder(n.left)
            print(n.data)
            self.inorder(n.right)

if __name__ == '__main__':
    tree = SplayTree()
    A = Node(10)
    B = Node(20)
    C = Node(30)
    tree.insert(A)
    tree.insert(B)
    tree.insert(C)
    tree.delete(A)
    tree.inorder(tree.root)