import pytest


class SeparateChainingHashTable:
    _MASK = 0x7fffffff
    _INIT_CAPACITY = 4

    def __init__(self, capacity=None):
        self._capacity = capacity or self._INIT_CAPACITY
        self._num_entries = 0
        self._data = [SequentialSearchSymbolTable()
                      for _ in range(self._capacity)]

    def __len__(self):
        return self._num_entries

    @property
    def empty(self):
        return len(self) == 0

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        return True

    def __getitem__(self, key):
        index = self._hash(key)
        return self._data[index][key]

    def __setitem__(self, key, value):
        if self._too_full():
            self._resize(2*self._capacity)

        index = self._hash(key)
        if key not in self._data[index]:
            self._num_entries += 1
        self._data[index][key] = value

    def pop(self, key):
        index = self._hash(key)
        if key not in self._data[index]:
            raise KeyError
        deleted = self._data[index].pop(key)
        self._num_entries -= 1
        if self._too_empty():
            self._resize(self._capacity//2)
        return deleted

    def _hash(self, key):
        """Hash function (depends on capacity).
        Returns a random int form 0 to _capacity with a (hopefully) uniform
        probability.
        Uses the native hash() to get the hash of a key, converts it to positive
        integer (masks the sign bit), and gets modulo by _capacity.
        """
        return (hash(key) & self._MASK) % self._capacity

    def _resize(self, new_size):
        """Create a new table with new capacity.
        Put all key-value pairs in it. Replace own state with its state.
        """
        tmp = self.__class__(new_size)
        for chain in self._data:
            for key, value in chain:
                tmp[key] = value
        self._capacity = tmp._capacity
        self._num_entries = tmp._num_entries
        self._data = tmp._data

    def _too_empty(self):
        """Check if should be resized to a smaller table"""
        return all([
            (self._capacity > self._INIT_CAPACITY),
            (self._num_entries <= 2 * self._capacity)
        ])

    def _too_full(self):
        """Check if should be resized to a larger table"""
        return (self._num_entries >= 10*self._capacity)


class SequentialSearchSymbolTable:

    def __init__(self):
        self._data = list()

    def __getitem__(self, key):
        """Look for the key sequentially; raise KeyError if not found"""
        for mykey, value in self._data:
            if mykey == key:
                return value
        raise KeyError

    def __setitem__(self, key, value):
        """Look for the item with the given key.
        If found, change its value to the new one.
        If not, add new key value pair.
        """
        for entry in self._data:
            if entry.key == key:
                entry.value = value
                break
        else:
            self._data.append(KeyValuePair(key, value))

    def __contains__(self, key):
        """Membership check"""
        for mykey, value in self._data:
            if mykey == key:
                return True
        return False

    def pop(self, key):
        for i, (mykey, _) in enumerate(self._data):
            if mykey == key:
                break
        else:
            raise KeyError
        return self._data.pop(i).value

    def __iter__(self):
        return iter(self._data)


class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __iter__(self):
        """Allows argument unpacking"""
        yield self.key
        yield self.value


@pytest.fixture
def table():
    return SeparateChainingHashTable()


def test_empty_table(table):
    assert len(table) == 0
    assert table.empty
    with pytest.raises(KeyError):
        table['foo']
    with pytest.raises(KeyError):
        table.pop('foo')


def test_set_item_and_get_it(table):
    table['foo'] = 'bar'
    assert table['foo'] == 'bar'
    assert len(table) == 1
    assert table.empty is False
    assert 'foo' in table


def test_resizing(table):
    for k, v in zip(range(50), range(1000, 1050)):
        table[k] = v
    assert len(table) == 50
    assert len(table._data) == 8


def test_pop_the_only_item(table):
    table['hello'] = 'world'
    assert table.pop('hello') == 'world'
    assert 'hello' not in table
    assert len(table) == 0


def test_pop_item_doesnt_affect_other_items(table):
    table[1] = 11
    table[2] = 22
    table[3] = 33
    table.pop(2)
    assert table[1] == 11
    assert table[3] == 33
    assert 2 not in table


def test_replace_value_for_a_key(table):
    table['foo'] = 'bar'
    table['foo'] = 'baz'
    assert table['foo'] == 'baz'
    assert len(table) == 1
