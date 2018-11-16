from math import log2, ceil

class Heap(object):
    ''' Base implementation of the heap data structure. To use, pass in a list
        of integers.

        Attributes:
            values: A list of integers holding the values of the heap.
    '''
    def __init__(self, values=[]):
        self.values = values

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        layers = list()
        height = ceil(log2(len(self.values)+1))
        for layer in range(height):
            first_padding = ' '*(2**(height-layer-1) - 1)
            inter_padding = ' '*(2**(height-layer) - 1)
            layers.append(first_padding + inter_padding.join([str(n) for n in self.values[(2**layer - 1):(2**(layer+1) - 1)]]))
        return '\n'.join(layers)

class MaxHeap(Heap):
    ''' Implementation of the max heap data structure. To use, pass in a list
        of integers.

        Attributes:
            values: A list of integers holding the values of the max heap
    '''
    def __init__(self, values=[]):
        self.build_max_heap(values)

    def build_max_heap(self, values):
        ''' From a list of integers, build up a max heap.

            Args:
                value: A list of integers to convert into a max heap.
        '''
        self.values = list()
        for value in values:
            self.insert_value(value)

    def insert_value(self, new_val):
        ''' Given the current state of the max heap, insert a new value while
            retaining the max heap property.

            Args:
                new_val: A new integer to insert into the current max heap.
        '''
        self.values.append(new_val)
        new_ind = len(self.values) - 1
        par_ind = (new_ind-1) // 2

        while self.values[par_ind] < self.values[new_ind] and new_ind != par_ind:
            self.values[par_ind], self.values[new_ind] = self.values[new_ind], self.values[par_ind]
            new_ind, par_ind = par_ind, max(0, par_ind-1) // 2

    def extract_max(self):
        ''' Given the current state of the max heap, extract the max value and
            fix the remainder so that it is still a max heap.

            Running this function will change the state of this object!

            Returns:
                max_val: The maximum value of the max heap.
        '''
        if len(self.values) < 1:
            return None

        self.values[0], self.values[-1] = self.values[-1], self.values[0]
        max_val = self.values[-1]
        self.values = self.values[:-1]

        index = 0
        while True:
            if 2*index + 1 >= len(self.values) or 2*index + 2 >= len(self.values):
                break

            if self.values[2*index + 1] >= self.values[2*index + 2]:
                child_ind = 2*index + 1
            else:
                child_ind = 2*index + 2

            if self.values[index] < self.values[child_ind]:
                self.values[index], self.values[child_ind] = self.values[child_ind], self.values[index]
                index = child_ind
            else:
                break

        return max_val
