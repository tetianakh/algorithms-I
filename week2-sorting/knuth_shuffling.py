import random

def shuffle(iterable):
    if not iterable:
        return []
    arr = list(iterable)
    for i in range(1, len(arr)):
        rand_idx = random.randint(0, i)
        arr[i], arr[rand_idx] = arr[rand_idx], arr[i]
    return arr

def test_shuffle_empty_array():
    assert [] == shuffle([])


def test_shuffle_single_element():
    assert [1] == shuffle([1])


def test_shuffle_with_random_seed():
    random.seed(0)
    assert [3, 2, 4, 6, 8, 1, 7, 9, 5, 0] == shuffle(range(10))

