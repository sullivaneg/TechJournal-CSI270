class ListBinaryTree:
    def __init__(self):
        self.tree = []  # List to store nodes

    def insert(self, data):
        """Insert at the next available position (maintains completeness)."""
        self.tree.append(data)

    def get_left_child(self, index):
        """Return left child index (or None if out of bounds)."""
        left_idx = 2 * index + 1
        return left_idx if left_idx < len(self.tree) else None

    def get_right_child(self, index):
        """Return right child index (or None if out of bounds)."""
        right_idx = 2 * index + 2
        return right_idx if right_idx < len(self.tree) else None

    def get_parent(self, index):
        """Return parent index (or None if root)."""
        if index == 0:
            return None
        return (index - 1) // 2



# Build a complete binary tree: [1, 2, 3, 4, 5]
list_tree = ListBinaryTree()
for data in [1, 2, 3, 4, 5]:
    list_tree.insert(data)

print("Root:", list_tree.tree[0])  # 1
print("Left child of root (index 0):", list_tree.tree[list_tree.get_left_child(0)])  # 2
print("Right child of root:", list_tree.tree[list_tree.get_right_child(0)])  # 3
print("Parent of node 4 (index 3):", list_tree.tree[list_tree.get_parent(3)])  # 2


# Min-heap (smallest element at root)
class MinHeap(ListBinaryTree):
    def heapify_up(self, index):
        """Move node up to maintain heap property."""
        parent = self.get_parent(index)
        if parent is not None and self.tree[index] < self.tree[parent]:
            # Swap with parent
            self.tree[index], self.tree[parent] = self.tree[parent], self.tree[index]
            self.heapify_up(parent)

    def insert(self, data):
        """Insert and heapify up."""
        super().insert(data)
        self.heapify_up(len(self.tree) - 1)

    # Usage


heap = MinHeap()
for num in [5, 3, 8, 1]:
    heap.insert(num)

print("Heap:", heap.tree)  # [1, 3, 8, 5] (root is smallest)