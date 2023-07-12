class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        min_val = self.heap.pop()
        self._bubble_down(0)
        return min_val

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            self._bubble_up(parent)

    def _bubble_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        min_child = index

        if left < len(self.heap) and self.heap[left] < self.heap[min_child]:
            min_child = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_child]:
            min_child = right

        if min_child != index:
            self._swap(index, min_child)
            self._bubble_down(min_child)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(7)
min_heap.insert(1)
print(min_heap.extract_min())
print(min_heap.extract_min())
print(min_heap.extract_min())
