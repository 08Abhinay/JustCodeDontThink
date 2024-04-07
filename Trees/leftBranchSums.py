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
    
def branchSums(root):
    # Write your code here.
    result_list = []
    branchSumsHelper(root, 0,  result_list)
    return result_list

def branchSumsHelper(root, running_sum,  result_list):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        result_list.append(running_sum + root.value)
        return 

    branchSumsHelper(root.left, running_sum + root.value, result_list)
    branchSumsHelper(root.right, running_sum + root.value, result_list)
  
