
def insertion_sort(iterable, sorted_fn=None):
    if sorted_fn is None:
        sorted_fn = lambda a, b: a < b
    arr = list(iterable)
    for i, elem in enumerate(arr[1:], 1):
        if sorted_fn(elem , arr[i-1]):
            j = i
            while sorted_fn(arr[j] , arr[j-1]) and j > 1:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1
    return arr


def test_insertion_empty_list():
    assert [] == insertion_sort([])


def test_insertion_alread_sorted():
    assert [1,2,3] == insertion_sort([1,2,3])


def test_insertion():
    assert [1, 2, 3] == insertion_sort([3, 2, 1])
