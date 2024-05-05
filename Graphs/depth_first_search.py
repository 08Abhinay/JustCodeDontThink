class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def dfsHelper(self, root, array):
        if root:
            array.append(root.name) #A,  
            total_children = len(root.children) #3
            if total_children == 0:
                return
            for i in range(total_children):
                self.dfsHelper(root.children[i], array)
        else:
            return
    def depthFirstSearch(self, array):
        # Write your code here.
        self.dfsHelper(self, array)
        
        return array



graph = Node("A")
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")


# print(graph.children[0].children[0].name)


print(graph.depthFirstSearch([]))

#OR Solution-2

# def depthFirstSearch(self, array):
#     array.append(self.name)

#     for child in self.children:
#         child.depthFirstSearch(array)
#     return array