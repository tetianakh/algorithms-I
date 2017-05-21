
def shell_sort(iterable, sorted_fn=lambda a, b: a < b):
    arr = list(iterable)
    h = 1
    while h < len(arr)/3:
        h = 3*h + 1
    while h > 0:
        for i in range(h, len(arr)):
            if sorted_fn(arr[i], arr[i-h]):
                j = i
                while sorted_fn(arr[j], arr[j-h]) and j > h:
                    arr[j-h], arr[j] = arr[j], arr[j-h]
                    j -= h
        h = h // 3
    return arr


def test_shell_empty_list():
    assert [] == shell_sort([])


def test_shell_alread_sorted():
    assert [1,2,3] == shell_sort([1,2,3])


def test_shell():
    assert [1, 2, 3] == shell_sort([3, 2, 1])

def test_shell_long():
    assert list(range(10)) == shell_sort([3, 9, 0, 8, 2, 7, 4, 6, 1, 5])
