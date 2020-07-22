"""
implementing a binary tree using Classes and References
"""


class BinaryTree(object):

    def __repr__(self):
        return "Root of tree is {0} \n" \
               "Left child is {1}\n" \
               "Right Child is {2}\n" .format(self.key, self.leftChild, self.rightChild)

    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.rightChild = self.rightChild
            self.rightChild = temp

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootValue(self, value):
        self.key = value

    def getRootValue(self):
        return self.key
    

# Function to traverse the tree using preorder method
def preorder(tree):
    if tree:
        print(tree.getRootValue())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
    else:
        print("debug")


# Function to traverse the tree using inorder method
def inorder(tree):
    inorder(tree.getLeftChild)
    print(tree.getRootValue)
    inorder(tree.getRightChild)


# Function to traverse the tree using postorder method
def postorder(tree):
    postorder(tree.getLeftChild)
    postorder(tree.getRightChild)
    print(tree.getRootValue)


tree1 = BinaryTree(23)

tree1.insertLeft(12)

tree1.insertLeft(14)

tree1.insertRight(78)

print(preorder(tree1))
