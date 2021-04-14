import io
import os

from math import floor


# https://github.com/atcoder/ac-library/blob/master/atcoder/lazysegtree.hpp
class LazySegTree:
    def __init__(self, _op, _e, _mapping, _composition, _id, v):
        def set(p, x):
            assert 0 <= p < _n
            p += _size
            for i in range(_log, 0, -1):
                _push(p >> i)
            _d[p] = x
            for i in range(1, _log + 1):
                _update(p >> i)

        def get(p):
            assert 0 <= p < _n
            p += _size
            for i in range(_log, 0, -1):
                _push(p >> i)
            return _d[p]

        def prod(l, r):
            assert 0 <= l <= r <= _n

            if l == r:
                return _e

            l += _size
            r += _size

            for i in range(_log, 0, -1):
                if ((l >> i) << i) != l:
                    _push(l >> i)
                if ((r >> i) << i) != r:
                    _push(r >> i)

            sml = _e
            smr = _e
            while l < r:
                if l & 1:
                    sml = _op(sml, _d[l])
                    l += 1
                if r & 1:
                    r -= 1
                    smr = _op(_d[r], smr)
                l >>= 1
                r >>= 1

            return _op(sml, smr)

        def apply(l, r, f):
            assert 0 <= l <= r <= _n
            if l == r:
                return

            l += _size
            r += _size

            for i in range(_log, 0, -1):
                if ((l >> i) << i) != l:
                    _push(l >> i)
                if ((r >> i) << i) != r:
                    _push((r - 1) >> i)

            l2 = l
            r2 = r
            while l < r:
                if l & 1:
                    _all_apply(l, f)
                    l += 1
                if r & 1:
                    r -= 1
                    _all_apply(r, f)
                l >>= 1
                r >>= 1
            l = l2
            r = r2

            for i in range(1, _log + 1):
                if ((l >> i) << i) != l:
                    _update(l >> i)
                if ((r >> i) << i) != r:
                    _update((r - 1) >> i)

        def _update(k):
            _d[k] = _op(_d[2 * k], _d[2 * k + 1])

        def _all_apply(k, f):
            _d[k] = _mapping(f, _d[k])
            if k < _size:
                _lz[k] = _composition(f, _lz[k])

        def _push(k):
            _all_apply(2 * k, _lz[k])
            _all_apply(2 * k + 1, _lz[k])
            _lz[k] = _id

        _n = len(v)
        _log = _n.bit_length()
        _size = 1 << _log
        _d = [_e] * (2 * _size)
        _lz = [_id] * _size
        for i in range(_n):
            _d[_size + i] = v[i]
        for i in range(_size - 1, 0, -1):
            _update(i)

        self.set = set
        self.get = get
        self.prod = prod
        self.apply = apply


MIL = 1 << 20


def makeNode(total, count):
    # Pack a pair into a float
    return (total * MIL) + count


def getTotal(node):
    return floor(node / MIL)


def getCount(node):
    return node - getTotal(node) * MIL


nodeIdentity = makeNode(0.0, 0.0)


def nodeOp(node1, node2):
    return node1 + node2
    # Equivalent to the following:
    return makeNode(
        getTotal(node1) + getTotal(node2), getCount(node1) + getCount(node2)
    )


identityMapping = -1


def mapping(tag, node):
    if tag == identityMapping:
        return node
    # If assigned, new total is the number assigned times count
    count = getCount(node)
    return makeNode(tag * count, count)


def composition(mapping1, mapping2):
    # If assigned multiple times, take first non-identity assignment
    return mapping1 if mapping1 != identityMapping else mapping2


def solve(N, Q, S, F, LR):
    segTree = LazySegTree(
        nodeOp,
        nodeIdentity,
        mapping,
        composition,
        identityMapping,
        [makeNode(float(d), 1.0) for d in F],
    )

    for l, r in LR[::-1]:
        l -= 1
        countOnes = getTotal(segTree.prod(l, r))
        countZeroes = r - l - countOnes
        if countZeroes > countOnes:
            # Majority were zeroes
            segTree.apply(l, r, 0)
        elif countZeroes < countOnes:
            # Majority were ones
            segTree.apply(l, r, 1)
        else:
            # No majority
            return "NO"
    for i in range(N):
        if getTotal(segTree.get(i)) != S[i]:
            return "NO"
    return "YES"


if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    TC = int(input())
    for tc in range(1, TC + 1):
        N, Q = [int(x) for x in input().split()]
        S = [int(d) for d in input().decode().rstrip()]
        F = [int(d) for d in input().decode().rstrip()]
        LR = [[int(x) for x in input().split()] for i in range(Q)]
        ans = solve(N, Q, S, F, LR)
        print(ans)