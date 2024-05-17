from tree_basic import Node
from tree_basic import Tree
from tree_basic import visualize_tree
import os


class BSTTree(Tree):
    def __init__(self, root: Node):
        self.root = root

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

    def searchByValue(self, value: int) -> Node:
        if not self.root:
            return None
        return self._searchByValue(self.root, value)

    def _searchByValue(self, node: Node, value: int) -> Node:
        if not node:
            return None
        if node.val == value:
            return node
        elif node.val > value:
            return self._searchByValue(node.left, value)
        else:
            return self._searchByValue(node.right, value)

    def insert(self, value: int):
        if not self.root:
            self.root = Node(value)
            return
        self._insert(self.root, value)

    def _insert(self, node: Node, value: int):
        if node.val == value:
            return
        elif node.val > value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
                return
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)

    def delete(self, value):
        parent, current = None, self.root
        while current:
            if current.val == value:
                break
            parent = current
            if current.val > value:
                current = current.left
            else:
                current = current.right

        if current is None:
            return
        l = current.left
        r = current.right
        if l is None or r is None:
            child = current.left or current.right
            if parent.left == current:
                parent.left = child
            else:
                parent.right = child
            if self.root == current:
                self.root = child
            current = None
        else:
            # 查找右子节点最小值
            min = r
            min_parent = current
            while min.left:
                min_parent = min
                min = min.left

            # 方法1 将整个左子树放到右子树的最小值的左边
            # min.left = l
            # current.val = r.val
            # current.left = r.left
            # current.right = r.right

            # 方法2 选择右子树中的最小值替代被删除节点
            self.delete(min.val)
            current.val = min.val
            # if min_parent != current:
            #     min.right = current.right
            #     min_parent.left = None
            # min.left = current.left

            # if parent:
            #     if parent.left == current:
            #         parent.left = min
            #     else:
            #         parent.right = min
            # if self.root == current:
            #     self.root = min
            # current = None


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


# print(searchByValue(root, 3))


print(tree.midSerach())
output_path=visualize_tree(tree).render("tree", format="png", view=False)
print(f"File saved to {output_path}")
print(f"Current directory contents: {os.listdir('.')}")
# insert(root, 2)
# insert(root, 5)
# insert(root, 100)
# insert(root, 1)
# midSerach(root)
# print(values)

# tree.delete(6)
# print(tree.root)
# print(n3)
# print(tree.midSerach())
