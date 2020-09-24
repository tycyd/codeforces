import Fenwick


class Cset:
    def __init__(self, discrete_data):
        discrete_data = set(discrete_data)
        self.restore = tuple(sorted(discrete_data))
        self.max_size = len(self.restore)
        self.size = 0
        self.discrete_dict = dict(zip(self.restore, range(self.max_size)))
        self.bit = Fenwick(self.max_size + 1)
        self.nums = [False] * (self.max_size + 1)

    def __getitem__(self, index):
        return self.restore[self.bit.findkth(index % self.size + 1)]

    def add(self, val):
        if val not in self.discrete_dict:
            return
        val = self.discrete_dict[val]
        if val < 0 or val > self.max_size or self.nums[val]:
            return
        self.size += 1
        self.bit.update(val, 1)
        self.nums[val] = True

    def discard(self, val):
        if val not in self.discrete_dict:
            return
        val = self.discrete_dict[val]
        if val < 0 or val > self.max_size or not self.nums[val]:
            return
        self.size -= 1
        self.bit.update(val, -1)
        self.nums[val] = False

    def bisect_left(self, val):
        """ index of val """
        return self.bit.query(self.discrete_dict[val])

    def bisect_right(self, val):
        return self.bit.query(self.discrete_dict[val] + 1)

    def lower(self, val):
        index = self.bisect_left(val)
        if index == 0:
            return None
        return self[index - 1]

    def higher(self, val):
        index = self.bisect_right(val)
        if index == self.size:
            return None
        return self[index]

    def __delitem__(self, index):
        val = self.bit.findkth(index % self.size + 1)
        self.size -= 1
        self.bit.update(val, -1)
        self.nums[val] = False

    def pop(self, index):
        val = self[index]
        del self[index]
        return val

    def __contains__(self, item):
        return self.nums[self.discrete_dict[item]]

    def __iter__(self):
        return (self.__getitem__(index) for index in range(self.size))

    def __repr__(self):
        return 'Cset({})'.format(list(self))

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.size > 0