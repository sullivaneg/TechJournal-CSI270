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

def verify_sum(root_values, partitions):
    if not partitions:
        return False

    sum_list = [0] * len(root_values)
    for partition in partitions:
        for i, num in enumerate(partition):
            sum_list[i] += num

    return sum_list == root_values

def check_partition(partitions, k, l):
    lst = []
    for entry in partitions:
        sum_constraint = sum(entry)
        diversity_constraint = len([x for x in entry if x > 0])
        if sum_constraint >= k and diversity_constraint >= l:
            lst.append(entry)
    return lst

# Get Max Depth
def match_constraints(root):
    """ Finds the max depth where all partitions satisfy constraints"""
    root_values = linked_list_to_list(root.list_head)
    depth = get_tree_depth(root)-1

    while depth >= 0:
        lists_at_depth = get_lists_at_depth(root, depth)

        if verify_sum(root_values, lists_at_depth):
            successful = check_partition(lists_at_depth, k, l)
            if len(successful) == len(lists_at_depth):
                return depth, successful
        depth -= 1
    return None, []

def get_nodes_at_depth(root, target_depth):
    """Get the nodes instead of the lists at a specific depth"""
    result = []

    def dfs(node, depth):
        """Recursive depth-first search"""
        if node is None:
            return
        if depth == target_depth:
            result.append(node)
            return
        dfs(node.left, depth+1)
        dfs(node.right, depth+1)

    dfs(root, 0)
    return result

def can_replace(node, k, l):
    """Checks if both children are valid partitions"""
    if not node.left or not node.right: # Need to have both children
        return False
    left_list = linked_list_to_list(node.left.list_head)
    right_list = linked_list_to_list(node.right.list_head)

    # Check if both children satisfy the constraints
    left_sum = sum(left_list)
    right_sum = sum(right_list)
    left_diversity = len([x for x in left_list if x>0])
    right_diversity = len([x for x in right_list if x>0])

    return left_sum >= k and left_diversity >= l and right_sum >= k and right_diversity >= l

def hybrid_algorithm(root, k, l):
    """
    I'm going to see if I can find the last level where everything matches and then by traversing down from the parent
    node to the children, replace nodes with children if children both match the specifications. (NOTE: I MIGHT JUST BE
    ABLE TO DO THIS)
    """
    root_values = linked_list_to_list(root.list_head)

    # Find initial valid level
    depth = get_tree_depth(root)-1
    valid_depth = None

    while depth >= 0:
        partitions = get_lists_at_depth(root, depth)

        if verify_sum(root_values, partitions):
            successful = check_partition(partitions, k, l)
            if len(successful) == len(partitions):
                valid_depth = depth
                break
        depth -= 1

    if valid_depth is None:
        return None, []

    # Get nodes at valid depth
    nodes_at_depth = get_nodes_at_depth(root, valid_depth)
    final = []

    for node in nodes_at_depth:
        if can_replace(node, k, l):
            # Substitute parent with both children
            left_partition = linked_list_to_list(node.left.list_head)
            right_partition = linked_list_to_list(node.right.list_head)
            final.append(left_partition)
            final.append(right_partition)
        else:
            final.append(linked_list_to_list(node.list_head))

        # Check
        if verify_sum(root_values, final):
            successful = check_partition(final, k, l)
            if len(successful) == len(final):
                return valid_depth, final

        # If it doesn't work
        return valid_depth, get_lists_at_depth(root, valid_depth)

# ---------------------------------------------------------------------
# Example usage (you can remove this part if you just want the structure)
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Root is a user-defined linked list
    l = 3
    k = 2
    root_values = [6,6,6,6,6,6]  # you can change this
    root = build_tree_from_list(root_values)
    depth, lists_at_depth = match_constraints(root)
    depth2, lists_at_depth2 = hybrid_algorithm(root, k, l)
    if lists_at_depth:
        print("Algorithm 1")
        print("Constraints met at depth {}".format(depth))
        print(lists_at_depth)
        print("________________________\n Algorithm 2")
        print("Constraints met at depth {}".format(depth2))
        print(lists_at_depth2)

    else:
        print("No Solution")


    # Visualize the entire tree
    #print_tree(root)

    # find the depth 'x' that satisfies the 2 conditions
    #lists_at_depth = get_lists_at_depth(root, x)
    #FILTER
    # If you reach a depth and it doesn't match the constraint, move up to the last level
    #print("Depth 2 lists:", lists_at_depth)

