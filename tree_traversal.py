class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=" ")
def preorder(root):
    if root:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)
root=node(1)
root.left=node(2)
root.left.left=node(3)
root.left.right=node(4)
root.right=node(5)
print("Inoder:")
inorder(root)
print("\nPreorder:")
preorder(root)
print("\nPost order:")
postorder(root)
