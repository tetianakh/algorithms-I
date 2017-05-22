import pytest


class Node:
    def __init__(self, key, value):
        self.right = None
        self.left = None
        self.value = value
        self.key = key

    def __repr__(self):
        return "Node(key=%s, value=%s, left=%s, right=%s)" % (
            self.key, self.value, self.left, self.right)

    @property
    def size(self):
        size = 1
        if self.right:
            size += self.right.size
        if self.left:
            size += self.left.size
        return size

    @property
    def depth(self):
        left = self.left.depth if self.left else 0
        right = self.right.depth if self.right else 0
        return 1 + max(right, left)

    def __contains__(self, key):
        if self.key == key:
            return True
        right = key in self.right if self.right else False
        left = key in self.left if self.left else False
        return right or left

    def __iter__(self):
        if self.left:
            for key in self.left:
                yield key
        yield self.key
        if self.right:
            for key in self.right:
                yield key

    def __getitem__(self, key):
        if self.key == key:
            return self.value
        if key > self.key and self.right:
            return self.right[key]
        if key < self.key and self.left:
            return self.left[key]
        raise KeyError


class BinarySearchTree:
    def __init__(self):
        self._root = None

    @property
    def size(self):
        if self._root:
            return self._root.size
        return 0

    @property
    def depth(self):
        if self._root:
            return self._root.depth
        return 0

    def get(self, key):
        x = self._root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.value
        return None

    def put(self, key, value):
        self._root = self._put(self._root, key, value)

    def _put(self, x, key, value):
        if x is None:
            return Node(key, value)
        if key < x.key:
            x.left = self._put(x.left, key, value)
        elif key > x.key:
            x.right = self._put(x.right, key, value)
        else:
            x.value = value
        return x

    def min(self):
        return self._min(self._root).key

    def _min(self, x):
        while x.left is not None:
            x = x.left
        return x

    def max(self):
        x = self._root
        while x.right is not None:
            x = x.right
        return x.key

    def delete(self, key):
        self._root = self._delete(self._root, key)

    def _delete(self, x, key):
        if x is None:
            return None
        if key < x.key:
            x.left = self._delete(x.left, key)
        elif key > x.key:
            x.right = self._delete(x.right, key)
        else:
            if x.right is None:
                return x.left
            if x.left is None:
                return x.right

            t = x
            x = self._min(t.right)
            x.right = self._delete_min(t.right)
            x.left = t.left
        return x

    def delete_min(self):
        self._root = self._delete_min(self._root)

    def _delete_min(self, x):
        if x.left is None:
            return None
        x.left = self._delete_min(x.left)
        return x

    def __contains__(self, key):
        if self._root:
            return key in self._root
        return False

    def __iter__(self):
        if self._root:
            return self._root.__iter__()
        return [].__iter__()

    def __getitem__(self, key):
        if self._root:
            return self._root[key]
        raise KeyError


def test_add_value_and_get_it():
    tree = BinarySearchTree()
    tree.put('a', 1)
    assert tree.get('a') == 1
    assert tree['a'] == 1

def test_get_nonexistent_key():
    tree = BinarySearchTree()
    assert tree.get('a') is None
    with pytest.raises(KeyError):
        tree['a']


def test_overwrite_value():
    tree = BinarySearchTree()
    tree.put('a', 1)
    tree.put('a', 2)
    assert tree.get('a') == 2
    assert tree['a'] == 2


def test_put_get_min_and_max():
    tree = BinarySearchTree()
    tree.put('m', 3)
    tree.put('f', 1)
    tree.put('z', 0)
    tree.put('p', 1)
    tree.put('a', 6)
    assert tree.min() == 'a'
    assert tree.max() == 'z'


def test_size_of_empty_tree_is_zero():
    tree = BinarySearchTree()
    assert tree.size == 0


def test_size_equals_to_num_distinct_elemetns():
    tree = BinarySearchTree()
    tree.put('a', 0)
    assert tree.size == 1
    tree.put('b', 0)
    assert tree.size == 2
    tree.put('b', 2)
    assert tree.size == 2


def test_depth_of_empty_tree_is_zero():
    tree = BinarySearchTree()
    assert tree.depth == 0


def test_depth_of_tree_worst_case():
    tree = BinarySearchTree()
    tree.put('a', 0)
    assert tree.depth == 1
    tree.put('b', 0)
    assert tree.depth == 2
    tree.put('c', 0)
    assert tree.depth == 3


def test_depth_of_tree_best_case():
    tree = BinarySearchTree()
    tree.put('d', 0)
    tree.put('f', 0)
    tree.put('g', 0)
    tree.put('e', 0)
    tree.put('b', 0)
    tree.put('a', 0)
    tree.put('c', 0)
    assert tree.depth == 3


def test_delete_min_with_one_element():
    tree = BinarySearchTree()
    tree.put('a', 1)
    tree.delete_min()
    assert tree.size == 0


def test_delete_min_with_multiple_elements():
    tree = BinarySearchTree()
    tree.put('d', 1)
    tree.put('f', 1)
    tree.put('c', 1)
    tree.put('b', 1)
    tree.put('a', 1)
    assert tree.min() == 'a'
    tree.delete_min()
    assert tree.size == 4
    assert tree.min() == 'b'


def test_delete_the_only_element():
    tree = BinarySearchTree()
    tree.put('a', 0)
    tree.delete('a')
    assert tree.size == 0
    assert 'a' not in tree


def test_delete_element_in_the_middle():
    tree = BinarySearchTree()
    tree.put('d', 1)
    tree.put('f', 1)
    tree.put('c', 1)
    tree.put('a', 1)
    assert tree.depth == 3
    assert 'c' in tree
    tree.delete('c')
    assert 'c' not in tree
    assert tree.depth == 2
    assert list(tree) == ['a', 'd', 'f']


def test_delete_root():
    tree = BinarySearchTree()
    tree.put('d', 1)
    tree.put('f', 1)
    tree.put('c', 1)
    tree.put('a', 1)
    tree.delete('d')
    assert 'd' not in tree
    assert list(tree) == ['a', 'c', 'f']


def test_iter_with_empty_tree_or_single_node():
    tree = BinarySearchTree()
    assert list(tree) == []
    tree.put('a', 0)
    assert list(tree) == ['a']


def test_iter_yields_keys_in_sorted_order():
    tree = BinarySearchTree()
    tree.put('d', 1)
    tree.put('f', 1)
    tree.put('c', 1)
    tree.put('a', 1)
    tree.put('k', 1)
    assert list(tree) == ['a', 'c', 'd', 'f', 'k']

