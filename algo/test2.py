class AVLTreeNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self._update_height(x)
        self._update_height(y)

        return y

    def _rebalance(self, node):
        self._update_height(node)

        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _insert(self, node, key, value):
        if not node:
            return AVLTreeNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        return self._rebalance(node)

    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)

        return self._rebalance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.key)
            self._in_order_traversal(node.right, result)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

# 创建一个AVL树实例
avl = AVLTree()

# 插入节点
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.insert(50)
avl.insert(25)

# 打印中序遍历结果
print("In-order traversal after inserts:", avl.in_order_traversal())

# 删除节点
avl.delete(40)
print("In-order traversal after deleting 40:", avl.in_order_traversal())

avl.delete(50)
print("In-order traversal after deleting 50:", avl.in_order_traversal())