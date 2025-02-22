"""
Breadth-First Search (BFS) is a fundamental algorithm used for traversing or
searching tree or graph data structures. It explores these structures level
by level, starting from a specified root node and proceeding through the
adjacent nodes.
### Characteristics of BFS:
1. **Level Order Traversal**:
    - BFS processes all nodes at the present "depth" or level before moving
    on to the nodes at the next depth level.
    - This means that it visits all the nodes of a given level before moving
    to the next level.

2. **Use of Queue**:
    - BFS uses a queue data structure to keep track of the nodes that need
    to be explored.
    - The queue helps ensure that nodes are processed in the order they are
    discovered, which guarantees that nodes closer to the root are processed
    first.

3. **Exploration Process**:
    - Start by enqueuing the root node.
    - Dequeue a node from the front of the queue and process it.
    - Enqueue all unvisited neighboring nodes (or children, in the case of
    trees) of the processed node.

4. **Applications**:
    - **Shortest Path (Unweighted Graphs)**: BFS is often used to find the
    shortest path in unweighted graphs.
    - **Level Order Traversal in Trees**: BFS provides a natural
    level-by-level traversal of a tree.
    - **Networking**: It is used in various network routing algorithms.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def bfs(root):
    if root is None:
        return

    queue = [root]  # Initialize the queue with the root node

    while queue:
        current_node = queue.pop(0)  # Dequeue the first node
        print(current_node.value)  # Process the current node

        # Enqueue the children of the current node
        for child in current_node.children:
            queue.append(child)


def print_tree(root, prefix="", is_last=True):
    if root is None:
        return

    # Print the current node
    print(prefix, "`- " if is_last else "|- ", root.value, sep="")
    prefix += "   " if is_last else "|  "

    # Process all children
    child_count = len(root.children)
    for idx, child in enumerate(root.children):
        # Recursively print each child
        print_tree(child, prefix, idx == (child_count - 1))


# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    child3 = TreeNode(4)
    root.children.extend([child1, child2])
    child1.children.append(child3)

    print("ASCII Diagram of Tree:")
    print_tree(root)

    bfs(root)
