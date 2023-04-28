
class Zero(Exception):
    pass

class Tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

a  = Tree(1)
b = Tree(0)
c = Tree(2)
a.left = b
a.right = c


def mul(root):
    try:
        if root.value == 0:
            raise Zero()
        elif root == None:
            return 1
        else:
            return root.value*mul(root.left)*mul(root.right)
    except Zero:
        return 0
mul(a)
