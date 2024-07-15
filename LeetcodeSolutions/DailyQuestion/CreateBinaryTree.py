class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_binary_tree(descriptions):
    node_map = {}
    child_nodes = set()

    for parent, child, is_left in descriptions:
        if parent not in node_map:
            node_map[parent] = TreeNode(parent)
        if child not in node_map:
            node_map[child] = TreeNode(child)

        parent_node = node_map[parent]
        child_node = node_map[child]

        if is_left == 1:
            parent_node.left = child_node
        else:
            parent_node.right = child_node

        child_nodes.add(child)

    # The root is the one node not in child_nodes
    root = next((node for node_val, node in node_map.items() if node_val not in child_nodes), None)

    return root

def level_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

root = create_binary_tree([(1, 2, 1), (1, 3, 0), (2, 4, 1), (2, 5, 0)])
print(level_traversal(root))  # [1, 2, 3, 4, 5]

