from pandas.io.formats.format import return_docstring


class ListNode:
    """Singly linked list node."""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"ListNode({self.value})"


def build_linked_list(values):
    """
    Create a singly linked list from a Python list of ints.
    Returns the head (ListNode).
    """
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def linked_list_to_list(head):
    """
    Convert a linked list (head: ListNode) back to a Python list.
    Useful for debugging / printing.
    """
    out = []
    curr = head
    while curr is not None:
        out.append(curr.value)
        curr = curr.next
    return out


class TreeNode:
    """
    Node of the binary tree.
    Each TreeNode holds:
      - list_head: head of a linked list (ListNode)
      - left: left child (TreeNode or None)
      - right: right child (TreeNode or None)
    """
    def __init__(self, list_head, left=None, right=None):
        self.list_head = list_head
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({linked_list_to_list(self.list_head)})"


def can_split_list(list_head):
    """
    Returns True if any element in the linked list is > 1,
    meaning further splitting is possible.
    """
    curr = list_head
    while curr is not None:
        if curr.value > 1:
            return True
        curr = curr.next
    return False


def split_list(list_head):
    """
    Given a linked list, split each element x into two values according to:
      - if x > 1:
          * even:  left = x // 2, right = x // 2
          * odd:   left = x // 2, right = x // 2 + 1
      - if x <= 1:
          * treated as not splittable
          * left = x, right = 0  (no further splits since x <= 1)

    Returns (left_head, right_head) where both are heads of new linked lists.
    """
    left_head = left_tail = None
    right_head = right_tail = None

    curr = list_head
    while curr is not None:
        x = curr.value

        if x > 1:
            base = x // 2
            if x % 2 == 0:
                left_val = base
                right_val = base
            else:
                left_val = base
                right_val = base + 1
        else:
            # x <= 1: no more splits
            left_val = x
            right_val = 0

        # Append to left list
        left_node = ListNode(left_val)
        if left_head is None:
            left_head = left_node
            left_tail = left_node
        else:
            left_tail.next = left_node
            left_tail = left_node

        # Append to right list
        right_node = ListNode(right_val)
        if right_head is None:
            right_head = right_node
            right_tail = right_node
        else:
            right_tail.next = right_node
            right_tail = right_node

        curr = curr.next

    return left_head, right_head


def _build_children(node):
    """
    Recursively build left and right children for a given TreeNode
    until no more splits are possible (all elements <= 1).
    """
    if node is None:
        return

    if not can_split_list(node.list_head):
        # Leaf node: nothing more to split
        return

    # Split current node's list into two child lists
    left_head, right_head = split_list(node.list_head)
    node.left = TreeNode(left_head)
    node.right = TreeNode(right_head)

    # Recurse
    _build_children(node.left)
    _build_children(node.right)


def build_tree_from_list(values):
    """
    Entry point.
    Takes a Python list of ints as the root linked list values,
    builds the entire binary tree according to the splitting rules,
    and returns the root TreeNode.
    """
    root_list = build_linked_list(values)
    root = TreeNode(root_list)
    _build_children(root)
    return root


def print_tree(node, level=0, side="root"):
    """
    Simple pre-order traversal to visualize the tree.
    Each node prints the list it stores.
    """
    # ADD AN IF ELSE CASE? DONT PRINT THE ENTIRE TREE
    if node is None:
        return
    indent = "  " * level
    print(f"{indent}{side}: {linked_list_to_list(node.list_head)}")
    print_tree(node.left, level + 1, "L")
    print_tree(node.right, level + 1, "R")

def get_tree_depth(node):
    if node is None:
        return 0
    return 1 + max(get_tree_depth(node.left), get_tree_depth(node.right))

def get_lists_at_depth(root, depth):
    """
    Return a list of linked lists (as Python lists) found at a specific depth.
    depth = 0 means the root.
    """
    if root is None:
        return []

    result = []

    def dfs(node, current_depth):  # (node, current_depth, k, l)
        if node is None:
            return
        if current_depth == depth:
            result.append(linked_list_to_list(node.list_head))
            return
        # continue deeper
        dfs(node.left, current_depth + 1)
        dfs(node.right, current_depth + 1)

    dfs(root, 0)
    return result

def add_lists(list1, list2):
    return [a+b for a, b in zip(list1, list2)]
# Get Max Depth
def match_constraints(root):
    depth = get_tree_depth(root)-1
    while depth >= 0:
        lists_at_depth = get_lists_at_depth(root, depth)
        successful = []
        sum_list = []
        for lst in lists_at_depth:
            for i in range(len(lst)):
                sum_list[i] = sum_list[i] + lst[i]
        if sum_list == root_values:
            for entry in lists_at_depth:
                sum_constraint = sum(entry)
                diversity_constraint = [x for x in entry if x > 0]
                if sum_constraint >= k:
                    if len(diversity_constraint) >= l:
                        successful.append(entry)
            if successful:
                return depth, successful
            else:
                depth -= 1
        else:
            depth -= 1
    if depth == 0:
        return depth, get_lists_at_depth(root, depth)
    if depth < 0:
        return None, []


# ---------------------------------------------------------------------
# Example usage (you can remove this part if you just want the structure)
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Root is a user-defined linked list
    l = 3
    k = 2
    root_values = [5, 2, 7, 6, 12]  # you can change this
    root = build_tree_from_list(root_values)
    depth, lists_at_depth = match_constraints(root)
    if lists_at_depth:
        print("Constraints met at depth {}".format(depth))
        print(lists_at_depth)
    else:
        print("No Solution")


    # Visualize the entire tree
    #print_tree(root)

    # find the depth 'x' that satisfies the 2 conditions
    #lists_at_depth = get_lists_at_depth(root, x)
    #FILTER
    # If you reach a depth and it doesn't match the constraint, move up to the last level
    #print("Depth 2 lists:", lists_at_depth)

