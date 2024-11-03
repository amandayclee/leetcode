class Heap:
    def __init__(self):
        self.heap = [0]  # dummy node at index 0
        
    def push(self, val):
        # Add new value to the end
        self.heap.append(val)
        
        # Sift up: move the new value to its correct position
        curr_idx = len(self.heap) - 1
        while curr_idx > 1 and self.heap[curr_idx] > self.heap[curr_idx // 2]:
            # Swap with parent if bigger
            parent_idx = curr_idx // 2
            self.heap[curr_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[curr_idx]
            curr_idx = parent_idx
            
    def pop(self):
        if len(self.heap) <= 1:  # empty heap
            return None
        if len(self.heap) == 2:  # only one element
            return self.heap.pop()
            
        # Save root value and move last element to root
        root_val = self.heap[1]
        self.heap[1] = self.heap.pop()
        
        # Sift down: move root to its correct position
        curr_idx = 1
        while 2 * curr_idx < len(self.heap):  # while has left child
            left_child = 2 * curr_idx
            right_child = 2 * curr_idx + 1
            
            # Determine which child to swap with
            swap_idx = left_child
            
            # Check if right child exists and is smaller
            if (right_child < len(self.heap) and  
                self.heap[curr_idx] > self.heap[right_child] and 
                self.heap[right_child] < self.heap[left_child]):
                swap_idx = right_child
                
            # Swap with left child if needed
            if self.heap[curr_idx] > self.heap[swap_idx]:
                self.heap[curr_idx], self.heap[swap_idx] = self.heap[swap_idx], self.heap[curr_idx]
                curr_idx = swap_idx
            else:  # heap property satisfied
                break
                
        return root_val