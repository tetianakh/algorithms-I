import pytest


def merge(a, aux, lo, mid, hi):
    for k in range(lo, hi+1):
        aux[k] = a[k]
    i, j = lo, mid+1
    for k in range(lo, hi+1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1

def test_merge_one_elem_array():
    arr = [1]
    merge(arr, list(arr), 0, 0, 0)
    assert arr == [1]

def test_two_elem_array():
    arr = [2,1]
    merge(arr, list(arr), 0, 0, 1)
    assert arr == [1,2]

def test_merge_two_elem_in_the_middle_of_array():
    arr = [4,3,2, 0, -1, 5]
    merge(arr, list(arr), 3, 3, 4)
    assert arr == [4,3,2,-1,0,5]

def test_merge_two_halves_of_array():
    arr = [4, 3, 2, 0, -1, 5, 7, -2]
    merge(arr, list(arr), 0, 3, 7)
    assert arr == [-1, 4, 3, 2, 0, 5, 7, -2]

@pytest.mark.current
def test_merge():
    arr = [8, 9, 6, 7]
    merge(arr, list(arr), 0, 1,3)
    assert arr == [6,7,8,9]

def sort_bottom_up(a):
    aux = list(a)
    step = 1;
    while step < len(a):
        for lo in range(0, len(a)-step, 2*step):
            merge(a, aux, lo, lo+step-1, min(lo+2*step-1, len(a)-1))
        step = step*2

@pytest.mark.parametrize(('array', 'expected'), [
    ([], []),
    ([1], [1]),
    ([2,1], [1,2]),
    ([4,2,-1], [-1, 2, 4]),
#    ([9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9]),
])
def test_sort_bottom_up(array, expected):
    sort_bottom_up(array)
    assert array == expected

