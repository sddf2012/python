from graphviz import Digraph


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.val!r},left:{self.left.val if self.left else 'None'},right:{self.right.val if self.right else 'None'})"


class BBSTNode(Node):
    def __init__(self, node: Node) -> None:
        self.val = node.val
        self.left = node.left
        self.right = node.right
        self.height = 0

    def __repr__(self):
        return f"Node({self.val!r},left:{self.left.val if self.left else 'None'},right:{self.right.val if self.right else 'None'},height:{self.height})"


class Tree:
    def __init__(self, root) -> None:
        self.root = root


def visualize_tree(tree: Tree):
    if not tree:
        return None
    dot = Digraph()
    add_nodes_edges(dot, tree.root)
    return dot


def add_nodes_edges(graph: Digraph, node: Node):
    if not node:
        return
    graph.node(str(node.val))
    while node.left:
        graph.edge(str(node.val), str(node.left.val))
        add_nodes_edges(graph, node.left)
    while node.right:
        graph.edge(str(node.val), str(node.right.val))
        add_nodes_edges(graph, node.right)
