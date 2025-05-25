import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        test_props = {"href": "https://www.google.com",
                      "target": "_blank"}
        
        node = HTMLNode("p", "This is a paragraph", None, test_props)
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"", node.props_to_html())
    
    
    def test_repr(self):
        node = HTMLNode("h1", "This is a header 1", None, None)
        self.assertEqual("HTMLNode: h1, This is a header 1, None, None", repr(node))
        
    
    def test_none(self):
        node = HTMLNode("h1", "This is a header 1")
        node2 = HTMLNode("h1", "This is a header 1", None, None)
        self.assertEqual(repr(node), repr(node2))
