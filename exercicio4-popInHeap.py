def pop(self):
    if not self.heap:
        return None
    min_val = self.heap[0]
    self.heap[0] = self.heap[-1]
    self.heap.pop()
    self.heapify_down(0)
    return min_val

