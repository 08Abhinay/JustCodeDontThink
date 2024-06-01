class Node(object):
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None 
        
if __name__ == '__main__':
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
    currentNode = root
    
    while currentNode is not None:
        if currentNode.value == value:
            return True
        elif currentNode.value > value:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
    return False

print(contains(root, 22))          

def value_to_left(root, value):
    
    pass
def remove(root, value, parentNode = None):
    currentNode = root
    while currentNode is not None:
        if value < currentNode.value:
            parentNode = currentNode
            currentNode = currentNode.left
        elif value > currentNode.value:
            parentNode = currentNode
            currentNode = currentNode.right
        else:
            if currentNode.left is not None and currentNode.right is not None:
                currentNode.value = currentNode.right.getMinValue() # This one keeps track of smallest number on the right
                currentNode.right.remove(currentNode.value, currentNode)
    pass

       
