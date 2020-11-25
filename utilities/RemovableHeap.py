from heapq import *


class RemovableHeap:
    def __init__(self, max_heap_type=None):
        if max_heap_type:  # element's class
            class Transform(max_heap_type):
                def __lt__(self, other):
                    return self >= other

            self._T = Transform
        else:
            self._T = lambda x: x
        self.heap = []
        self.rem = []
        self.dict = {}
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        self.__trim()
        return self.heap[index]

    def push(self, val):
        val = self._T(val)
        heappush(self.heap, val)
        if val in self.dict:
            self.dict[val] += 1
        else:
            self.dict[val] = 1
        self.size += 1

    def pop(self):
        self.__trim()
        if not self.heap:
            return None
        self.size -= 1
        val = heappop(self.heap)
        if self.dict[val] == 1:
            del self.dict[val]
        else:
            self.dict[val] -= 1
        return val

    def remove(self, val):
        val = self._T(val)
        if val not in self.dict:
            return
        self.size -= 1
        if self.dict[val] == 1:
            del self.dict[val]
        else:
            self.dict[val] -= 1
        heappush(self.rem, val)

    def __trim(self):
        while self.rem and self.rem[0] == self.heap[0]:
            heappop(self.heap)
            heappop(self.rem)
