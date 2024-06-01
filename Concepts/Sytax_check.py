class Node(object):
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None 
        
if __name__ == '__main__':
    # root = Node('F')
    # root.left = Node('B')
    # root.right = Node('G')
    # root.left.left = Node('A')
    # root.left.right = Node('D')
    # root.right.right = Node('I')
    # root.left.right.left=Node('C')
    # root.left.right.right = Node('E')
    # root.right.right.left = Node('H')
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(2)
    root.left.left.left = Node(1)
    root.left.right = Node(5)
    root.right = Node(15)
    root.right.left = Node(13)
    root.right.left.right = Node(14)
    root.right.right = Node(22)

def insert(root, value):
    
    currentNode = root
    while True:
        if value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = Node(value)
                break
            else:
                currentNode = currentNode.left
        else:
            if currentNode.right is None:
                currentNode.right = Node(value)
                break
            else:
                currentNode = currentNode.right
    return root
    
insert(root, 25)


def contains(root, value):
    pass

def pre_order_traversal(root):
    
    if root is None:
        return
    
    print(root.value, end=' ')
    pre_order_traversal(root.left)    
    pre_order_traversal(root.right)

# def in_order_traversal(root):
     
#     if root:

#         in_order_traversal(root.left)
#         print(root.value, end=' ')
#         in_order_traversal(root.right)
 
# def post_order_traversal(root):
   
#     if root:

#         in_order_traversal(root.left)
#         in_order_traversal(root.right)
#         print(root.value, end=' ')
#     pass



# Function call
# print("Preorder traversal of binary tree is:")
pre_order_traversal(root) 
# print()
# in_order_traversal(root)
# print()
# post_order_traversal(root)




    


