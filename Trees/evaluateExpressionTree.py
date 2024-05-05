import operator
class Node(object):
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None 


# root = Node(10)
# root.left = Node(5)
# root.left.left = Node(2)
# root.left.left.left = Node(1)
# root.left.right = Node(5)
# root.right = Node(15)
# root.right.left = Node(13)
# root.right.left.right = Node(14)
# root.right.right = Node(22)

root = Node(-1)
root.left = Node(2)
root.right = Node(3)


def evaluateExpressionTree(tree):
    # Write your code here.
    # if tree.value == -1 or tree.value == -2:
    #     result = 0
    # else:
    #     result = 1
    return evaluate(tree)
    
def evaluate(tree):
    operators = {
        '-1': operator.mul,
        '-2': operator.sub,
        '-4': operator.mul,
        '-3': operator.truediv
    }
    if tree.value < 0:
        operation_function = operators.get(str(tree.value))
    
        left_result = evaluate(tree.left)
        right_result = evaluate(tree.right)
        
        return operation_function(left_result, right_result)
    else:
        # If it's an operand (non-negative value), return its value
        return tree.value


print(evaluateExpressionTree(root))

#Solution-2
# import operator

# class BinaryTree:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


# def evaluateExpressionTree(tree):
#     # Write your code here.
#     return evaluate(tree)
    
# def evaluate(tree):
   
#     if tree.value < 0:
#         left_operation = evaluate(tree.left)
#         right_operation = evaluate(tree.right)

#         if tree.value == -1:
#             return left_operation + right_operation
#         elif tree.value == -2:
#             return left_operation - right_operation
#         elif tree.value == -3:
#             return int(left_operation / right_operation)
#         elif tree.value == -4:
#             return left_operation * right_operation
        
#     else:
#         return tree.value

    
    
 
