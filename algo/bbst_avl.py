from algo.tree_basic import Node
from algo.tree_basic import BBSTNode
from tree_basic import Tree

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
        if node is None:
            return None
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

    def _sorted_list_to_avl(self, nodes: List[Node], start: int, end: int):
        if start > end:
            return None
        mid = (start + end) // 2
        node = BBSTNode(nodes[mid])
        node.left = self._sorted_list_to_avl(nodes, start, mid - 1)
        node.right = self._sorted_list_to_avl(nodes, mid + 1, end)
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        return node

    def bst_to_avl(self, bst_tree: BSTTree):
        if not bst_tree:
            return None
        nodes = bst_tree.midSerach()
        return AvlTree(self._sorted_list_to_avl, nodes, 0, len(nodes) - 1)

