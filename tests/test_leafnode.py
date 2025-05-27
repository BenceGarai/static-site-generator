import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_props(self):
        test_leaf_node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", test_leaf_node.to_html())
        
    
    def test_to_html_with_props(self):
        test_props = {"href": "https://www.google.com"}
        test_leaf_node = LeafNode("a", "Click me!", test_props)
        self.assertEqual("<a href=\"https://www.google.com\">Click me!</a>", test_leaf_node.to_html())
        