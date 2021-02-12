class Heap():

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def add(self, data):
        self.heap.append(data)
        self.size += 1
        self._float(self.size)           

    def _float(self, current):

        parent = current // 2

        if self.heap[current] > self.heap[parent]:
            return
        self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
        self._float(parent)

    def pop(self):

        try:
            self.heap[self.size], self.heap[1] = self.heap[1], self.heap[self.size]
            last_element = self.heap.pop(self.size)
            self.size -= 1
            self._pop(1)

            return last_element

        except Exception as error:
            print(error)

    def _pop(self, current_index):

        left = current_index * 2
        right = current_index * 2 + 1

        if left > self.size:
            return
        elif right > self.size:
            index = left
        elif self.heap[left] > self.heap[right]:
            index = right
        else:
            index = left

        if self.heap[current_index] > self.heap[index]:           
            self.heap[current_index], self.heap[index] = self.heap[index], self.heap[current_index]
            self._pop(index)
        return
    
    def peek(self):
        return self.heap[1]

    def xprint(self):
        print(self.heap[1:])
    



