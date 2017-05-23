import pytest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __iter__(self):
        yield self
        if self.next:
            for node in self.next:
                yield node

    def __getitem__(self, index):
        for i, node in enumerate(self):
            if i == index:
                return node
        raise IndexError("List index out of range")

    def __setitem__(self, index, new_node):
        node = self[index-1]
        new_node.next = node.next.next
        node.next = new_node

    def insert(self, index, new_node):
        node = self[index-1]
        new_node.next = node.next
        node.next = new_node

    def pop(self, index):
        node = self[index-1]
        deleted = node.next
        node.next = node.next.next
        return deleted



class LinkedList:
    def __init__(self):
        self._root = None
        self._length = 0

    def append(self, value):
        self.insert(self._length, value)

    def __len__(self):
        return self._length

    def __iter__(self):
        if self._root:
            return (n.value for n in self._root)
        return iter([])

    def __getitem__(self, index):
        if len(self) <= index:
            raise IndexError
        return self._root[index].value

    def __setitem__(self, index, value):
        if len(self) <= index:
            raise IndexError("Assignemnt out of range")
        new = Node(value)
        if index == 0:
            new.next = self._root.next
            self._root = new
        else:
            self._root[index] = new

    def insert(self, index, value):
        if index > self._length:
            raise IndexError("List index out of range")
        new = Node(value)
        if self._root:
            self._root.insert(index, new)
        else:
            self._root = new
        self._length += 1

    def pop(self, index):
        if index >= self._length:
                raise IndexError("List index out of range")
        if index == 0:
            deleted = self._root
            self._root = self._root.next
        else:
            deleted = self._root.pop(index)
        return deleted.value


@pytest.fixture
def llist():
    return LinkedList()


def test_empty_list(llist):
    assert list(llist) == []
    assert len(llist) == 0


def test_add_element(llist):
    llist.append('hello')
    assert list(llist) == ['hello']
    assert llist[0] == 'hello'
    assert len(llist) == 1


def test_add_two_elements(llist):
    llist.append('hello')
    llist.append('hello')
    assert list(llist) == ['hello', 'hello']
    assert len(llist) == 2


def test_set_element(llist):
    llist.append('hello')
    assert llist[0] == 'hello'
    llist[0] = 'world'
    assert list(llist) == ['world']


def test_insert_element(llist):
    llist.append('foo')
    llist.append('baz')
    llist.insert(1, 'bar')
    assert list(llist) == ['foo', 'bar', 'baz']


@pytest.fixture
def three_elem_llist(llist):
    llist.append('foo')
    llist.append('bar')
    llist.append('baz')
    return llist


def test_delete_root_element(three_elem_llist):
    assert three_elem_llist.pop(0) == 'foo'
    assert list(three_elem_llist) == ['bar', 'baz']


def test_delete_element_in_the_middle(three_elem_llist):
    assert three_elem_llist.pop(1) == 'bar'
    assert list(three_elem_llist) == ['foo', 'baz']


def test_delete_last_element(three_elem_llist):
    assert three_elem_llist.pop(2) == 'baz'
    assert list(three_elem_llist) == ['foo', 'bar']
