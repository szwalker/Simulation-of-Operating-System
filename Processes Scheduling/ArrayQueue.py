class EmptyCollection(Exception):
    pass

class ArrayQueue:
    INIT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INIT_CAPACITY
        self.front_ind = 0
        self.num_of_elems = 0

    def __len__(self):
        return self.num_of_elems

    # special method to prevent same process appearing multiple times in Q
    def __contains__(self,item):
        flag = False
        for j in self.data:
            if item is j:
                return True
        return flag

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems  += 1

    def dequeue(self):
        if (self.is_empty()):
            raise EmptyCollection("Queue is empty")
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return elem

    def front(self):
        if (self.is_empty()):
            raise EmptyCollection("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0