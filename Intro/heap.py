
class Heap:
    def __init__(self,):
        self.heap = []

    def add(self, element):
        self.heap.append(element)
        
        i = len(self.heap) - 1
        while i > 0:
            if self.heap[i] <= self.heap[int(i/2)]:
                break
            else:
                self.heap[i], self.heap[int(i/2)] = self.heap[int(i/2)], self.heap[i]
                i = int(i/2)

    def pop(self):
        result = self.heap[0]
        i = len(self.heap) - 1

        self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
        self.heap.pop(i)

        i = 0
        while (2*i + 1) < len(self.heap):
            index = None

            if 2*i + 2 < len(self.heap):
                if self.heap[i] < self.heap[2*i + 1] or self.heap[i] < self.heap[2*i + 2]: 
                    if self.heap[2*i + 1] >= self.heap[2*i + 2]:
                        index = 2*i + 1
                    else:
                        index = 2*i + 2
            else:
                if self.heap[i] < self.heap[2*i + 1]:
                    index = 2*i + 1
            
            self.heap[i], self.heap[index] = self.heap[index], self.heap[i]
            i = index

        return result




def main():
    h = Heap()

    h.add(22)
    h.add(65)
    h.add(10)
    h.add(20)
    h.add(30)
    h.add(15)
    h.add(35)

    arr = []
    arr.append(h.pop())
    arr.append(h.pop())
    arr.append(h.pop())
    arr.append(h.pop())
    arr.append(h.pop())
    arr.append(h.pop())
    arr.append(h.pop())

    print(arr)


main()