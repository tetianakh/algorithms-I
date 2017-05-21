from shell_sort import shell_sort
import random

def rand_range():
    while True:
        yield random.random()

def shuffle(iterable):
    if not iterable:
        return []
    mapping = {k: v for k, v in zip(rand_range(), iterable)}
    return [mapping[k] for k in shell_sort(mapping.keys())]


def test_shuffle_empty_list():
    assert [] == shuffle([])


def test_shuffle_one_element():
    assert [1] == shuffle([1])

def test_with_rand_seed():
    random.seed(0)
    assert [0, 3, 7, 5, 2, 8, 4, 9, 1, 6] == shuffle(range(10))
    random.seed(1)
    assert [0, 9, 8, 3, 5, 4, 6, 2, 7, 1] == shuffle(range(10))
