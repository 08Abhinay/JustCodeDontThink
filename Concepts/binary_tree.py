class Node(object):
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None 
        
def pre_order_traversal(root):
    
    if root is None:
        return
    
    print(root.value, end=' ')
    pre_order_traversal(root.left)    
    pre_order_traversal(root.right)

def in_order_traversal(root):
     
    if root:

        in_order_traversal(root.left)
        print(root.value, end=' ')
        in_order_traversal(root.right)
 
def post_order_traversal(root):
   
    if root:

        in_order_traversal(root.left)
        in_order_traversal(root.right)
        print(root.value, end=' ')
    pass

if __name__ == '__main__':
    root = Node('F')
    root.left = Node('B')
    root.right = Node('G')
    root.left.left = Node('A')
    root.left.right = Node('D')
    root.right.right = Node('I')
    root.left.right.left=Node('C')
    root.left.right.right = Node('E')
    root.right.right.left = Node('H')


# Function call
print("Preorder traversal of binary tree is:")
pre_order_traversal(root) 
print()
in_order_traversal(root)
print()
post_order_traversal(root)




    


