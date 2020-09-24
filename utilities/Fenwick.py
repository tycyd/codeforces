class Fenwick:
    """ Simpler FenwickTree """

    def __init__(self, x):
        self.bit = [0] * x

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """
        Find largest idx such that sum(bit[:idx]) < k
        (!) different from pyrival (just removed the '=')
        """
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k > self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1