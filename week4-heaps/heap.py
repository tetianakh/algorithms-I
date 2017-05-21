import pytest


class MaxHeap:
    def __init__(self):
        self._data = list([None])

    def delMax(self):
        self._exchange(1, self._last_idx)
        max_key = self._data.pop()
        self._sink(1)
        return max_key

    def insert(self, key):
        self._data.append(key)
        self._swim(self._last_idx)

    def is_empty(self):
        return self._last_idx == 0

    @property
    def _last_idx(self):
        return len(self._data) - 1

    def _sink(self, k):
        N = self._last_idx

        while 2*k <= N:
            j = 2*k
            if (j < N) and self._less(j, j+1):
                j += 1
            if not self._less(k, j):
                break
            self._exchange(k, j)
            k = j

    def _swim(self, k):
        while k//2 >= 1:
            j = k//2
            if self._less(k, j):
                break
            self._exchange(k, j)
            k = j

    def _less(self, idx1, idx2):
        return self._data[idx1] < self._data[idx2]

    def _exchange(self, idx1, idx2):
        self._data[idx1], self._data[idx2] = self._data[idx2], self._data[idx1]


@pytest.fixture
def hq():
    return MaxHeap()


def test_insert_single_element(hq):
    hq.insert(1)
    assert hq.delMax() == 1


def test_delMax_returns_max_elem(hq):
    hq.insert(2)
    hq.insert(3)
    hq.insert(1)
    assert hq.delMax() == 3
    assert hq.delMax() == 2
    assert hq.delMax() == 1


def test_empty_heap_is_empty(hq):
    assert hq.is_empty()


def test_heap_with_one_element_is_not_empty(hq):
    hq.insert(1)
    assert not hq.is_empty()
