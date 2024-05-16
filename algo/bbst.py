class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return f"Node({self.val!r},left:{self.left.val if self.left else 'None'},right:{self.right.val if self.right else 'None'})"

    def height(self):
        if self is None:
            return -1
        return self.height

    def update_height(self):
        return max(self.height(self.left), self.height(self.right)) + 1


class Tree:
    def __init__(self, root: Node):
        self.root = root
