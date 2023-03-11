class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
n1=BinaryTreeNode(50)
n2=BinaryTreeNode(20)
n3=BinaryTreeNode(45)
n4=BinaryTreeNode(11)
n5=BinaryTreeNode(15)
n6=BinaryTreeNode(30)
n7=BinaryTreeNode(78)

n1.leftchild=n2
n1.rightchild=n3
n2.leftchild=n4
n2.rightchild=n5
n3.leftchild=n6
n3.rightchild=n7

print(n1.data)
print(n1.leftchild.data)
print(n1.rightchild.data)
print(n2.leftchild.data)
print(n2.rightchild.data)
print(n3.leftchild.data)
print(n3.rightchild.data)
