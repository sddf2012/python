from tree_basic import Node
from tree_basic import BBSTNode
from tree_basic import Tree
from tree_basic import plot_tree
from binary_search_tree import BSTTree

from typing import List


class AvlTree(Tree):
    def __init__(self, root: BBSTNode):
        self.root = root

    def _height(self, node: BBSTNode):
        if node is None:
            return -1
        return node.height

    def _update_height(self, node: BBSTNode):
        if node is None:
            return
        node.height = max(self._height(node.left), self._height(node.right)) + 1

    def _balance_factor(self, node: BBSTNode):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _re_blance(self, node: BBSTNode):
        # if node is None:
        #     return None
        self._update_height(node)
        bf = self._balance_factor(node)

        if bf > 1:
            if self._balance_factor(node.left) < 0:
                # 先左旋后右旋
                node.left = self._left_rorate(node.left)
            return self._right_rorate(node)
        elif bf < -1:
            if self._balance_factor(node.right) > 0:
                # 先右旋后左旋
                node.right = self._right_rorate(node.right)
            return self._left_rorate(node)
        return node

    def _right_rorate(self, node: BBSTNode) -> BBSTNode:
        child_l = node.left
        chilf_l_r = child_l.right

        child_l.right = node
        node.left = chilf_l_r

        self._update_height(node)
        self._update_height(child_l)
        return child_l

    def _left_rorate(self, node: BBSTNode):
        child_r = node.right
        child_r_l = child_r.left

        child_r.left = node
        node.right = child_r_l

        self._update_height(node)
        self._update_height(child_r)
        return child_r

    def _insert(self, node, value):
        if not node:
            return BBSTNode(val=value)
        if value < node.val:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return self._re_blance(node)

    def insert(self, value=None):
        self.root = self._insert(self.root, value)

    def midSerach(self) -> list:
        if not self.root:
            return None
        values = []
        self._midSerach(self.root, values)
        return values

    def _midSerach(self, node: Node, values):
        if node.left:
            self._midSerach(node.left, values)
        values.append(node.val)
        if node.right:
            self._midSerach(node.right, values)


def _sorted_list_to_avl(nodes: list, start: int, end: int):
    if start > end:
        return None
    mid = (start + end) // 2
    node = BBSTNode(node=nodes[mid])
    node.left = _sorted_list_to_avl(nodes, start, mid - 1)
    node.right = _sorted_list_to_avl(nodes, mid + 1, end)
    node.height = 1 + max(height(node.left), height(node.right))
    return node


def height(node: Node):
    if node is None:
        return -1
    return node.height


def bst_to_avl(bst_tree: BSTTree):
    if not bst_tree:
        return None
    nodes = bst_tree.midSerach()
    return AvlTree(_sorted_list_to_avl(nodes, 0, len(nodes) - 1))


n1 = Node(1)
n3 = Node(3)
n4 = Node(4)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n10 = Node(10)
n13 = Node(13)
n14 = Node(14)

n8.left = n3
n8.right = n10
n3.left = n1
n3.right = n6
n6.left = n4
n6.right = n7
n10.right = n14
n14.left = n13

tree = BSTTree(n8)
avlTree = bst_to_avl(tree)
# plot_tree(avlTree)
avlTree.insert(5)
print(avlTree.midSerach())
plot_tree(avlTree)
