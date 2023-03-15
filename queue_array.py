class Queue:

    def __init__(self, capacity=0):
        self.cap = capacity
        self.front = 0
        self.back = 0
        self.num_items = 0
        self.items = [None] * capacity

    def is_empty(self):
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        return self.num_items == self.cap

    def enqueue(self, item):
        if self.is_full():
            raise IndexError
        else:
            self.num_items += 1
            if self.back > (self.cap - 1):
                self.back = 0
            self.items[self.back] = item
            self.back += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        else:
            temp = self.items[self.front]
            self.front += 1
            if self.front > self.cap - 1:
                self.front = 0
            self.num_items -= 1
            return temp

    def size(self):
        return self.num_items

    def see_queue(self):
        print(self.items)
