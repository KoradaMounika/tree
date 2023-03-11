class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if(key<node.key):
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def minval(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current
def delnode(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left=delnode(root.left,key)
    elif key>root.key:
        root.right=delnode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minval(root.right)
        root.key=temp.key
        root.right=delnode(root.right,temp.key)
    return root
root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)
print("inorder traversal:")
inorder(root)
print("delete 20:")
root=delnode(root,20)
inorder(root)
print("delete 30:")
root=delnode(root,30)
inorder(root)
print("delete 50:")
root=delnode(root,50)
inorder(root)
























        
        
