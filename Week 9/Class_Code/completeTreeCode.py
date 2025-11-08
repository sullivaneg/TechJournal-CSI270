#The code below is found at: https://www.guvi.in/blog/crud-operations-on-binary-trees-using-python
#Author: Suman Gangopadhyay

class Node:
    '''

        val : Stores data of Node

        left : Reference to Left Child Node

        right : Reference to Right Child Node

    '''

    def __init__(self, val):
        self.val = val

        self.right = None

        self.left = None


class RealBinaryTree:

    # root : Reference to the root node of tree

    def __init__(self):

        self.root = None

    def insert_node(self, data):

        if self.root is None:

            self.root = Node(data)

        else:

            self.__insert__recursive(self.root, data)

    def __insert__recursive(self, node, data):

        if data < node.val:

            if node.left is None:

                node.left = Node(data)

            else:

                self.__insert__recursive(node.left, data)

        else:

            if node.right is None:

                node.right = Node(data)

            else:

                self.__insert__recursive(node.right, data)

    def print_tree(self, node, level=0):

        if node is not None:
            self.print_tree(node.right, level + 1)

            print(' ' *4 * level + '->', node.val)

            self.print_tree(node.left, level + 1)


if __name__ == '__main__':
    # Creating the binary tree

    tree = RealBinaryTree()

    tree.root = Node(10)  # Root node

    # Level 1

    tree.root.left = Node(20)

    tree.root.right = Node(30)

    # Level 2

    tree.root.left.left = Node(40)

    tree.root.left.right = Node(50)

    tree.root.right.left = Node(60)

    tree.root.right.right = Node(70)

    # Level 3

    tree.root.right.right.left = Node(80)

    tree.root.right.right.right = Node(90)

    # Print the binary tree

    tree.print_tree(tree.root)

'''
Let’s break down and describe each part of the given code in detail. The code defines a binary tree structure and provides functionality to insert nodes and print the tree.

class Node:


        val : Stores data of Node

        left : Reference to Left Child Node

        right : Reference to Right Child Node
'''


def __init__(self, val):
    self.val = val

    self.right = None

    self.left = None


'''
Description:

Purpose: The Node class encapsulates the properties and behaviors of each node within a binary tree. Each node stores a value and has references to its left and right child nodes.
Attributes:
val: Stores the data of the node.
left: Reference to the left child node (initially set to None).
right: Reference to the right child node (initially set to None).
Constructor: The __init__ method initializes a new node with the given value and sets its left and right child references to None.
'''


class RealBinaryTree:

    # root : Reference to the root node of tree

    def __init__(self):

        self.root = None

    def insert_node(self, data):

        if self.root is None:

            self.root = Node(data)

        else:

            self.__insert__recursive(self.root, data)

    def __insert__recursive(self, node, data):

        if data < node.val:

            if node.left is None:

                node.left = Node(data)

            else:

                self.__insert__recursive(node.left, data)

        else:

            if node.right is None:

                node.right = Node(data)

            else:

                self.__insert__recursive(node.right, data)

    def print_tree(self, node, level=0):

        if node is not None:
            self.print_tree(node.right, level + 1)

            print(' ' *4 * level + '->', node.val)

            self.print_tree(node.left, level + 1)


'''
Description:

Purpose: The RealBinaryTree class manages the structure and operations of the binary tree, such as inserting nodes and printing the tree.
Attributes:
root: Reference to the root node of the tree (initially set to None).
Constructor: The __init__ method initializes an empty binary tree with the root set to None.
Methods:
insert_node(self, data): Inserts a node with the given data into the binary tree.
If the tree is empty (root is None), the new node becomes the root.
Otherwise, it calls the helper method __insert__recursive to insert the node recursively.
__insert__recursive(self, node, data): A helper method to insert a node recursively.
If the given data is less than the current node’s value, it goes to the left subtree.
If the given data is greater than or equal to the current node’s value, it goes to the right subtree.
If the appropriate child node is None, it creates a new node with the given data.
print_tree(self, node, level=0): Prints the binary tree in a structured format.
It recursively prints the right subtree, the current node, and then the left subtree.
Uses indentation to represent the level of the tree.
'''

# Main function

if __name__ == '__main__':
    # Creating the binary tree

    tree = RealBinaryTree()

    tree.root = Node(10)  # Root node

    # Level 1

    tree.root.left = Node(20)

    tree.root.right = Node(30)

    # Level 2

    tree.root.left.left = Node(40)

    tree.root.left.right = Node(50)

    tree.root.right.left = Node(60)

    tree.root.right.right = Node(70)

    # Level 3

    tree.root.right.right.left = Node(80)

    tree.root.right.right.right = Node(90)

    # Print the binary tree

    tree.print_tree(tree.root)

'''
Description:

Purpose: This block of code creates a binary tree and demonstrates the insertion and printing of nodes.
Tree Construction:
A RealBinaryTree object tree is created.
The root node is initialized with a value of 10.
Nodes are inserted manually to build the tree with values at different levels.
Level 1 nodes: 20 (left) and 30 (right).
Level 2 nodes: 40 (left-left), 50 (left-right), 60 (right-left), 70 (right-right).
Level 3 nodes: 80 (right-right-left), 90 (right-right-right).
Printing the Tree:
The print_tree method is called to print the structure of the binary tree.
The Output

The Output
This format helps visualize the hierarchical structure of the binary tree, showing the relationships between parent and child nodes at different levels.

MDN
Updating Nodes in a Binary Tree
Updating a node in a binary tree involves modifying the value of an existing node while ensuring the tree’s structural integrity and properties remain intact.
This operation begins with locating the target node using a traversal method such as in-order, pre-order, or post-order traversal. Once the node is identified,
its value is updated with the new data. It’s crucial to ensure that this update does not disrupt the binary tree’s properties. For instance, in a binary search tree (BST),
the left subtree must contain nodes with values less than the parent node, and the right subtree must contain nodes with values greater. After updating a node’s value,
maintaining these properties might require additional adjustments, such as reordering or rebalancing the tree.

Now, before we dive deeper into the coding aspects of node updates, if you’re looking to build a strong foundation in Python and data structures,
learning Python from scratch is a great place to start. Check out GUVI’s Python course which will guide you through everything from basic operations
to complex implementations, including tree structures and beyond. You can enroll directly here to start your journey.

Below is a given Python code which will demonstrate the updation of a Binary Tree node. Here, we are using Python to create a Binary Tree whose Root Node is 10.
Under Root Node there will be two child nodes 20 and 30. Now, insert node 40 and 50 inside node 20 and 60 and 70 inside node 30.  Create a method that can edit
a particular node just by giving the old node data and new node data.



Using Python Create a Binary Tree whose Root Node is 10.  

Under Root Node there will be two child nodes 20 and 30.

Now, insert node 40 and 50 inside node 20 and 60 and 70 inside node 30.

Create a method that can edit a particular node just by giving the old node data and new node data.

'''


class Node:

    def __init__(self, val):
        self.val = val

        self.right = None

        self.left = None


class RealBinaryTree:

    def __init__(self):

        self.root = None

    def insert_node(self, data):

        if self.root is None:

            self.root = Node(data)

        else:

            self.__insert__recursive(self.root, data)

    def __insert__recursive(self, node, data):

        if data < node.val:

            if node.left is None:

                node.left = Node(data)

            else:

                self.__insert__recursive(node.left, data)

        else:

            if node.right is None:

                node.right = Node(data)

            else:

                self.__insert__recursive(node.right, data)

    def print_tree(self, node, level=0):

        if node is not None:
            self.print_tree(node.right, level + 1)

            print(' ' *4 * level + '->', node.val)

            self.print_tree(node.left, level + 1)

    def edit_node(self, node, old_data, new_data):

        if node is None:
            return False

        # Check if the current node contains the data to be edited

        if node.val == old_data:
            node.val = new_data

            return True

        # Recursively check left and right subtrees

        return self.edit_node(node.left, old_data, new_data) or self.edit_node(node.right, old_data, new_data)


if __name__ == '__main__':

    # Creating the binary tree

    tree = RealBinaryTree()

    tree.root = Node(10)  # Root node

    # Level 1

    tree.root.left = Node(20)

    tree.root.right = Node(30)

    # Level 2

    tree.root.left.left = Node(40)

    tree.root.left.right = Node(50)

    tree.root.right.left = Node(60)

    tree.root.right.right = Node(70)

    # Print tree before editing

    print('Tree before editing:')

    tree.print_tree(tree.root)

    # Edit node

    old_data = 40

    new_data = 100

    if tree.edit_node(tree.root, old_data, new_data):

        print(f'Node with value {old_data} was edited to {new_data}.')

    else:

        print(f'Node with value {old_data} was not found.')

    # Print tree after editing

    print('Tree after editing:')

    tree.print_tree(tree.root)

'''
Class Node:

Purpose: Represents a single node in the binary tree.
Attributes:
val: Stores the data value of the node.
left: Points to the left child node.
right: Points to the right child node.
Class RealBinaryTree:

Purpose: Manages the binary tree and provides operations for insertion, printing, and editing nodes.
Methods:
__init__(self): Initializes an empty binary tree by setting the root node to None.
insert_node(self, data):
If the tree is empty, it creates a new root node with the given data.
Otherwise, call the recursive __insert__recursive method to find the appropriate position for the new node based on its value.
__insert__recursive(self, node, data):
Recursively traverses the tree to find the correct position for the new node.
If the new data is less than the current node’s data, it’s inserted into the left subtree.
If the new data is greater than or equal to the current node’s data, it’s inserted into the right subtree.
print_tree(self, node, level=0):
Recursively traverses the tree and prints each node’s value with appropriate indentation.
edit_node(self, node, old_data, new_data):
Recursively searches for the node with the old_data value.
If found, update the node’s value to new_data.
Returns True if the node is edited, False otherwise.
Main Execution:

Tree Creation:
A binary tree is created with the root node having the value 10.
Child nodes are added to create a binary tree structure.

Tree Printing:
The print_tree method is used to display the tree structure before editing.

Node Editing:
The edit_node method is called to find and modify the node with the value 40 to 100.

Tree Printing (Post-Edit):
The print_tree method is called again to display the modified tree structure.

The Output
Deleting a Node from a Binary Tree
Deleting a node from a binary tree involves three primary cases: 
removing a leaf node, removing a node with one child, and removing a node with two children.
In the first case, the node is simply removed. In the second case, the node is replaced by its child.
The third case, which is the most complex, involves finding the node’s in-order predecessor or successor
to replace the deleted node while maintaining the tree’s structure. This ensures the binary tree’s
properties are preserved. Efficiently handling deletions is crucial for maintaining the tree’s balance and performance.

Below is a given Python code which will demonstrate the updation of a Binary Tree node. Here,
we are using Python to create a Binary Tree Using Python Create a Binary Tree whose Root Node is 10.
Under Root Node there will be two child nodes 20 and 30. Now, insert node 40 and 50 inside node 20 and
60 and 70 inside node 30. Create a Delete method that will delete  a particular node when it exists inside the tree.



Using Python Create a Binary Tree whose Root Node is 10. Under Root Node there will be two child nodes 20 and 30.
Now, insert node 40 and 50 inside node 20 and 60 and 70 inside node 30. Create a Delete method that will delete
a particular node when it exists inside the tree

'''
class Node:

    def __init__(self, val):
        self.val = val

        self.right = None

        self.left = None


class RealBinaryTree:

    def __init__(self):

        self.root = None

    def insert_node(self, data):

        if self.root is None:

            self.root = Node(data)

        else:

            self.__insert__recursive(self.root, data)

    def __insert__recursive(self, node, data):

        if data < node.val:

            if node.left is None:

                node.left = Node(data)

            else:

                self.__insert__recursive(node.left, data)

        else:

            if node.right is None:

                node.right = Node(data)

            else:

                self.__insert__recursive(node.right, data)

    def print_tree(self, node, level=0):

        if node is not None:
            self.print_tree(node.right, level + 1)

            print(' ' *4 * level + '->', node.val)

            self.print_tree(node.left, level + 1)

    def find_min(self, node):

        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete_node(self, node, key):

        if node is None:
            return node

        # Traverse to find the node to delete

        if key < node.val:

            node.left = self.delete_node(node.left, key)

        elif key > node.val:

            node.right = self.delete_node(node.right, key)

        else:

            # Case 1: Node with only one child or no child

            if node.left is None:

                return node.right

            elif node.right is None:

                return node.left

            # Case 2: Node with two children, get the inorder successor

            min_node = self.find_min(node.right)

            node.val = min_node.val

            node.right = self.delete_node(node.right, min_node.val)

        return node


if __name__ == '__main__':
    # Creating the binary tree

    tree = RealBinaryTree()

    tree.root = Node(10)  # Root node

    # Level 1

    tree.root.left = Node(20)

    tree.root.right = Node(30)

    # Level 2

    tree.root.left.left = Node(40)

    tree.root.left.right = Node(50)

    tree.root.right.left = Node(60)

    tree.root.right.right = Node(70)

    # Print tree before deletion

    print('Tree before deletion:')

    tree.print_tree(tree.root)

    # Delete a node

    key_to_delete = 30

    tree.root = tree.delete_node(tree.root, key_to_delete)

    print(f'\nNode with value {key_to_delete} was deleted.\n')

    # Print tree after deletion

    print('Tree after deletion:')

    tree.print_tree(tree.root)

'''
This Python code implements a binary search tree (BST) data structure with basic
operations like insertion, deletion, and printing.

Key Classes and Methods:

Node Class:
Represents a single node in the binary tree.
Stores the node’s value (val), left child (left), and right child (right).

RealBinaryTree Class:
insert_node(data):
Inserts a new node with the given data into the tree.
If the tree is empty, creates a new root node. Otherwise, recursively traverses
the tree to find the appropriate position for the new node based on its value.

print_tree(node, level=0):
Recursively prints the tree in a visually appealing format, with indentation representing the tree’s levels.

find_min(node):
Finds the minimum value node in the subtree rooted at the given node.

delete_node(node, key):
Deletes the node with the given key from the tree.

Handles three cases:
Node to be deleted is not found.
Node to be deleted has one or no child.
Node to be deleted has two children. In this case,
the in order successor (the smallest value in the right subtree)
is found and used to replace the deleted node.

Main Execution Block:

Creates a binary tree with the specified structure.
Prints the tree before deletion.
Deletes the node with the value 30.
Prints the tree after deletion.
Key Points:

Binary Search Tree Property: The left subtree of a node contains values less than the node’s value,
and the right subtree contains values greater than the node’s value.

The Output
MDN
Conclusion
Mastering CRUD operations in binary trees goes beyond just writing code, it’s about understanding
the logic behind each operation. Efficient insertion and retrieval techniques ensure fast data access,
while proper update and delete methods maintain the tree’s structural integrity. Whether
you’re working on a simple project or designing a complex database system, knowing how
to handle these operations can significantly improve your approach to data management.

By implementing these techniques in Python, you can develop a solid foundation in tree-based
algorithms and gain a deeper appreciation for their efficiency. As you continue exploring
advanced concepts like balancing and traversal optimizations,
these CRUD operations will serve as a strong base for building more
sophisticated data structures.
'''