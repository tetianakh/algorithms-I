def partition(arr, lo, hi):
    i, j = lo, hi+1
    while True:
        i += 1
        while (i < hi) and (arr[i] < arr[lo]):
            i += 1
        j -= 1
        while arr[lo] < arr[j]:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]
    return j


def test_partition():
    arr = [2, 1, 3]
    result = partition(arr, 0, 1)
    assert result == 1
    assert arr == [1, 2, 3]

def test_partition_duplicate_keys():
    arr = [3, 3, 3, 3]
    result = partition(arr, 0, 1)
    assert result == 1
    assert arr == [3, 3, 3, 3]
