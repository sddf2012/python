import matplotlib.pyplot as plt


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.val!r},left:{self.left.val if self.left else 'None'},right:{self.right.val if self.right else 'None'})"


class BBSTNode(Node):
    def __init__(self, node: Node = None, val=None) -> None:
        if node:
            self.val = node.val
            self.left = node.left
            self.right = node.right
        if val:
            self.val = val
            self.left = None
            self.right = None
        self.height = 0

    def __repr__(self):
        return f"Node({self.val!r},left:{self.left.val if self.left else 'None'},right:{self.right.val if self.right else 'None'},height:{self.height})"


class Tree:
    def __init__(self, root) -> None:
        self.root = root


def _plot_tree(node, x=0, y=0, dx=1, dy=1, ax=None):
    if ax is None:
        fig, ax = plt.subplots()

    if node is not None:
        ax.text(
            x,
            y,
            str(node.val),
            ha="center",
            va="center",
            bbox=dict(facecolor="white", edgecolor="black", boxstyle="circle"),
        )

        if node.left is not None:
            ax.plot([x, x - dx], [y, y - dy], "k-")
            _plot_tree(node.left, x - dx, y - dy, dx / 2, dy, ax)

        if node.right is not None:
            ax.plot([x, x + dx], [y, y - dy], "k-")
            _plot_tree(node.right, x + dx, y - dy, dx / 2, dy, ax)
    return ax


def plot_tree(tree: Tree):
    ax = _plot_tree(tree.root)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.show()
