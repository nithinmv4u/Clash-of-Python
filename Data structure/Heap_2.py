class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        max_val = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] < self.heap[index]:
            self._swap(parent, index)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self._swap(largest, index)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# Example usage:
max_heap = MaxHeap()
max_heap.insert(5)
max_heap.insert(3)
max_heap.insert(7)
max_heap.insert(1)
print(max_heap.extract_max())  # Output: 7
print(max_heap.extract_max())  # Output: 5
print(max_heap.extract_max())  # Output: 3
