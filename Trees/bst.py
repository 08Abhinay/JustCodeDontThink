
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
    
def findClosestValueInBst(tree, target):
    
    return findClosestHelper(tree, target, float("inf"))
    
def findClosestHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestHelper(tree.right, target, closest) 
    else:
        return closest
   

result = findClosestValueInBst(root, 12)
print(result)