class Node(object):
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None 


root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.right = Node(5)
root.right = Node(15)
root.right.left = Node(13)
root.right.left.right = Node(14)
root.right.right = Node(22)

def nodeDepths(root):
    
    depths = 0
    running_sum = 0 
    depths = nodeDepthsHelper(root, depths )
    return depths
    
def nodeDepthsHelper(root, depths):
    
    # if root is None:
    #     return 0
    # return depths + nodeDepthsHelper(root.left, depths + 1) + nodeDepthsHelper(root.right, depths + 1)
    if root is None:
        return 0
    # Debug print to show the current node and its depth
    print(f"Visiting Node with Value: {root.value}, at Depth: {depths}")
    # Recursively call for left and right children, adding 1 to the depth
    left_depth_sum = nodeDepthsHelper(root.left, depths + 1)
    right_depth_sum = nodeDepthsHelper(root.right, depths+ 1)
    # Calculate the total depth sum for the current subtree
    total_depth_sum = depths + left_depth_sum + right_depth_sum
    # Debug print to show how the depth sums are accumulated
    print(f"Node Value: {root.value}, Depth: {depths}, Total Depth Sum including children: {total_depth_sum}")
    return total_depth_sum


print(nodeDepths(root))

