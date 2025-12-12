#Author: Emma Sullivan
# Class: CSI-270-01
# Certification of Authenticity:
# I certify that this is entirely my own work, except where I have given fully documented
# references to the work of others. I understand the definition and consequences of
# plagiarism and acknowledge that the assessor of this assignment may, for the purpose of
# assessing this assignment reproduce this assignment and provide a copy to another member
# of academic staff and / or communicate a copy of this assignment to a plagiarism checking
# service(which may then retain a copy of this assignment on its database for the purpose
# of future plagiarism checking).

# Problem Statement
#Implement those two searches and compare their performances.
# For comparison, pick 10 random numbers (or letters, whatever your tree stores) and use one of the searches above
# to find each of those 10 numbers in the tree. In the process count the number of comparisons it took to find each of
# 10 numbers and report the average number of comparisons for 10 searches both for breadth-first search
# and depth-first search.

import random
from collections import deque

# Tree Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Helper Function
def build_tree(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = build_tree(root.left, value)
    else:
        root.right = build_tree(root.right, value)

    return root

def bfs(root, target):
    if not root:
        return False, 0

    queue = deque([root])
    comparisons = 0

    while queue:
        node = queue.popleft()
        comparisons += 1

        if node.value == target:
            return True, comparisons

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return False, comparisons

def dfs(root, target):
    if not root:
        return False, 0

    stack = [root]
    comparisons = 0

    while stack:
        node = stack.pop()
        comparisons += 1

        if node.value == target:
            return True, comparisons

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return False, comparisons



# TEST

# Build the tree
nums = random.sample(range(1, 60), 30)
root = None
for v in nums:
    root = build_tree(root, v)

# Pick 10 search targets
targets = random.sample(range(1, 60), 10)

print("Tree values:", nums)
print("Search targets:", targets)

bfs_counts = []
dfs_counts = []

for t in targets:
    root_temp, bfs_comparisons = bfs(root, t)
    root_temp, dfs_comparisons = dfs(root, t)

    bfs_counts.append(bfs_comparisons)
    dfs_counts.append(dfs_comparisons)

print("Breadth First Search Comparisons:", bfs_counts)
print("Depth-First Search Comparisons:", dfs_counts)

print("Average BFS comparisons:", sum(bfs_counts) / len(bfs_counts))
print("Average DFS comparisons:", sum(dfs_counts) / len(dfs_counts))