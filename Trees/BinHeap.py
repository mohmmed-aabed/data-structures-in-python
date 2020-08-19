class BinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_down(self, i):
        while i * 2 <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tem = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tem
            i = mc

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def build_heap(self, lst):
        i = len(lst) // 2
        self.current_size = len(lst)
        self.heap_list = [0] + lst[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1


my_heap = BinHeap()
my_heap.build_heap([8, 5, 4, 11, 2, 10, 7, 9, 6, 12, 3])
print(my_heap.heap_list)
# [0, 2, 3, 4, 6, 5, 10, 7, 9, 11, 12, 8]

print(my_heap.del_min())
# 2
print(my_heap.heap_list)
# [0, 3, 5, 4, 6, 8, 10, 7, 9, 11, 12]

my_heap.insert(1)
print(my_heap.heap_list)
# [0, 1, 3, 4, 6, 5, 10, 7, 9, 11, 12, 8]
