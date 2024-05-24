from tree_basic import Node
from tree_basic import Tree
from tree_basic import plot_tree


class MaxHeap:
    def __init__(self, heap=None) -> None:
        if heap:
            self.heap = heap
            for i in range(len(heap) // 2 - 1, -1, -1):
                self.heapify(i)
        else:
            self.heap = []

    def _parent(self, index) -> int:
        return (index - 1) // 2

    def _left(self, index) -> int:
        return index * 2 + 1

    def _right(self, index) -> int:
        return index * 2 + 2

    def is_empty(self) -> bool:
        return len(self.heap) < 1

    def peek(self):
        return None if self.is_empty() else self.heap[0]

    def heapify(self, idx):
        left = self._left(idx)
        right = self._right(idx)

        length = len(self.heap)
        max_idx = idx
        if left < length and self.heap[max_idx] < self.heap[left]:
            max_idx = left
        if right < length and self.heap[max_idx] < self.heap[right]:
            max_idx = right

        if idx != max_idx:
            self.heap[max_idx], self.heap[idx] = self.heap[idx], self.heap[max_idx]
            self.heapify(max_idx)

    def push(self, value):
        self.heap.append(value)
        idx = len(self.heap) - 1
        parent_index = self._parent(idx)
        while parent_index >= 0:
            if value > self.heap[parent_index]:
                self.heap[idx] = self.heap[parent_index]
                self.heap[parent_index] = value
                idx = parent_index
                parent_index = self._parent(parent_index)
            else:
                break

    def pop(self):
        length = len(self.heap)
        if length < 1:
            return
        if length == 1:
            del self.heap[0]

        value = self.heap[length - 1]
        self.heap[0] = value
        del self.heap[length - 1]
        self.heapify(0)

    def heap_to_tree(self) -> Tree:
        root = self._heap_to_tree(0)
        if not root:
            return None
        return Tree(root)

    def _heap_to_tree(self, idx) -> Node:
        if idx > len(self.heap) - 1:
            return None
        node = Node(self.heap[idx])
        node.left = self._heap_to_tree(self._left(idx))
        node.right = self._heap_to_tree(self._right(idx))
        return node


heap = MaxHeap()
heap.heap = [50, 30, 40, 10, 20, 35, 15]
# plot_tree(heap.heap_to_tree())

# print(heap.is_empty())
# print(heap.peek())
# heap.push(16)
# heap.push(17)
# heap.push(18)
# heap.push(100)
# heap.push(200)
heap.pop()
heap.pop()
heap.pop()

print(heap.peek())
plot_tree(heap.heap_to_tree())

# h2 = MaxHeap([4, 10, 3, 5, 1, 12, 15, 19, 1, 100])
# plot_tree(h2.heap_to_tree())
