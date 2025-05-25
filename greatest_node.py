from binary_tree import Node


def greatest_node(root:Node):
    node_large = root.value
    if root.left_child is not None:
        if greatest_node(root.left_child) > node_large:
            node_large = greatest_node(root.left_child)
    if root.right_child is not None:
        if greatest_node(root.right_child) > node_large:
            node_large = greatest_node(root.right_child)
    return node_large

    return node


if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))