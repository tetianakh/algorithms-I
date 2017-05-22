import enum
import pytest


class LinkColor(enum.Enum):
    RED = 1
    BLACK = 2


class Node:
    def __init__(self, key, value, color):
        self.key = key
        self.value = value
        self.color = color   # color of parent link
        self.right = None
        self.left = None


class RedBlackTree:
    def __init__(self):
        self._root = None

    def __setitem__(self, key, value):
        self._root = self._put(self._root, key, value)

    def _put(self, node, key, value):
        if node is None:
            return Node(key, value, LinkColor.RED)
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)

        return node

    def _is_red(self, node):
        return node.color == LinkColor.RED if node else False

    def _rotate_left(self, node):
        rotated = node.right
        node.right = rotated.left
        rotated.left = node
        rotated.color = node.color
        node.color = LinkColor.RED
        return rotated

    def _rotate_right(self, node):
        rotated = node.left
        node.left = rotated.right
        rotated.right = node
        rotated.color = node.color
        node.color = LinkColor.RED
        return rotated

    def _flip_colors(self, node):
        """Split temporary 4-node into two 2-nodes"""
        node.color = LinkColor.RED
        node.left.color = LinkColor.BLACK
        node.right.color = LinkColor.BLACK


@pytest.fixture
def tree():
    return RedBlackTree()


class TestRedBlackTreeInternals:
    """Make sure RB tree is implemented correctly.

    Verifies relative ordering of nodes, their values and colors.
    """

    def test_add_item_to_empty_tree(self, tree):
        tree['a'] = 1
        assert tree._root.value == 1
        assert tree._root.key == 'a'

    def test_add_two_items_rotate_left(self, tree):
        tree['a'] = 1
        tree['b'] = 0
        assert tree._root.value == 0
        assert tree._root.key == 'b'
        assert tree._root.left.key == 'a'
        assert tree._root.left.color == LinkColor.RED

    def test_add_three_items_double_rotation_and_flip(self, tree):
        tree['c'] = 1
        tree['a'] = 0
        tree['b'] = 2
        assert tree._root.value == 2
        assert tree._root.key == 'b'
        assert tree._root.left.color == LinkColor.BLACK
        assert tree._root.left.key == 'a'
        assert tree._root.right.color == LinkColor.BLACK
        assert tree._root.right.key == 'c'
