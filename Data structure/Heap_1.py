class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        print(len(self.heap))
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        min_val = self.heap.pop()
        self._heapify_down(0)  
        return min_val

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        print(parent,index)
        if parent >= 0 and self.heap[parent] > self.heap[index]:
            print("swap")
            self._swap(parent, index)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self._swap(smallest, index)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# Example usage:
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(7)
min_heap.insert(1)
min_heap.insert(4)
min_heap.insert(8)
print(min_heap.extract_min())  # Output: 1
print(min_heap.extract_min())  # Output: 3
print(min_heap.extract_min())  # Output: 5
