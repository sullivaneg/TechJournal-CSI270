class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def switch(self, data):
        self.data = data
        L = self.leftChild.data
        R = self.rightChild.data
        self.rightChild = L
        self.leftChild = R
        print(node3.leftChild.data, node3.rightChild.data)



class NewTreeStructure:
    def __init__(self, data):
        self.data = data
        self.firstNode = None
        self.secondNode = None
        self.thirdNode = None
        self.fourthNode = None

#Data assignment - all data is integer except for '' that represents no data assigned
node1 = BinaryTreeNode(50)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(1)
node4 = BinaryTreeNode(4)
node5 = BinaryTreeNode(5)
node6 = BinaryTreeNode(6)


#References
node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node3.leftChild = node6
node3.rightChild = node5

#Assumes prior knowledge of tree structure





print("Root Node is:")
print(node1.data)

print("The left child of the node",node1.data," is:")
print(node1.leftChild.data)

print("The right child of the node",node1.data," is:")
print(node1.rightChild.data)

print("Node is:")
print(node2.data)

print("left child of the node is:")
print(node2.leftChild.data)

print("Node is:")
print(node3.data)

print("left child of the node is:")
print(node3.leftChild.data)

print("right child of the node is:")
print(node3.rightChild.data)

print("Node is:")
print(node4.data)

print("left child of the node is:")
print(node4.leftChild)

print("right child of the node is:")
print(node4.rightChild)

print("Node is:")
print(node5.data)

print("left child of the node is:")
print(node5.leftChild)

print("right child of the node is:")
print(node5.rightChild)

print("Node is:")
print(node6.data)

print("left child of the node is:")
print(node6.leftChild)

print("right child of the node is:")
print(node6.rightChild)
