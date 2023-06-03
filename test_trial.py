import unittest
from unittest import TestCase
from trial import validateBst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        self.assertEqual(validateBst(root), True)
if __name__=='__main__':
    unittest.main()

