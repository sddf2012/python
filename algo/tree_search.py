import queue


class Node:
    def __init__(self, val: str) -> None:
        self.val = val
        self.left = None
        self.right = None

    # def setLeft(self, left) -> None:
    #     self.left = left

    # def setRight(self, right) -> None:
    #     self.right = right


values = []

q = queue.Queue()


def seq(node: Node):
    q.put(node)
    while not q.empty():
        item = q.get()
        values.append(item.val)
        if item.left:
            q.put(item.left)
        if item.right:
            q.put(item.right)


def front(node: Node):
    values.append(node.val)
    if node.left:
        front(node.left)
    if node.right:
        front(node.right)


def mid(node: Node):
    if node.left:
        mid(node.left)
    values.append(node.val)
    if node.right:
        mid(node.right)


def after(node: Node):
    if node.left:
        after(node.left)
    if node.right:
        after(node.right)
    values.append(node.val)


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
i = Node("I")

f.left = b
f.right = g
b.left = a
b.right = d
d.left = c
d.right = e
g.right = i
i.left = h

seq(f)
print(values)
values.clear()

front(f)
print(values)
values.clear()
mid(f)
print(values)
values.clear()
after(f)
print(values)
