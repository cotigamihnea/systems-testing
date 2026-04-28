import unittest
from tree import Tree
from node import Node

class TestTreeFind(unittest.TestCase):
    
    def setUp(self):
        """Setup initial logic: create a tree and populate it before each test"""
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(1)
        self.tree.add(4)

    def test_find_existing_node(self):
        """Test finding a node that exists in the tree"""
        result_node = self.tree.find(4)
        
        self.assertIsNotNone(result_node)
        self.assertEqual(result_node.data, 4)

    def test_find_non_existing_node(self):
        """Test finding a node that does NOT exist in the tree"""
        result_node = self.tree.find(10)
        
        self.assertIsNone(result_node)

if __name__ == '__main__':
    unittest.main()