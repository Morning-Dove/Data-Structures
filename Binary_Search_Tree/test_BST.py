import pytest
import unittest

from Binary_Search_Tree.BST import BinarySearchTree as BST

@pytest.fixture
def bst():
    tree = BST()
    tree.insert(10)
    tree.insert(7)
    tree.insert(16)
    tree.insert(3)
    tree.insert(8)
    return tree

def test_insert(bst):
    assert bst.root.value == 10
    assert bst.root.left.value == 7
    assert bst.root.right.value == 16
    assert bst.root.left.left.value == 3
    assert bst.root.left.right.value == 8

def test_search(bst):
    assert bst.search(7) == True
    assert bst.search(16) == True
    assert bst.search(3) == True
    assert bst.search(8) == True
    assert bst.search(11) == False

def test_in_order_traversal(bst):
    assert bst.in_order_traversal() == [3, 7, 8, 10, 16]

def test_find_min(bst):
    assert bst.find_min() == 3

def test_find_max(bst):
    assert bst.find_max() == 16

def test_height(bst):
    assert bst.height() == 3

def test_count_leaves(bst):
    assert bst.count_leaves() == 3

def test_serialize(bst):
    assert bst.serialize() == "10,7,3,8,16"

def test_deserialize():
    tree = BST()
    tree.deserialize("10,7,3,8,16")
    assert tree.in_order_traversal() == [3, 7, 8, 10, 16]


