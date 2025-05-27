import unittest
from converters import text_node_to_html_node
from textnode import TextType, TextNode


class TestConverters(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    
    def test_image(self):
        node = TextNode("Click this image!", TextType.IMAGE, "www.google.com/coolimage.jpeg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.google.com/coolimage.jpeg", "alt": "alttext"})
        
        
    def test_link(self):
        node = TextNode("Click me!", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me!")
        self.assertEqual(html_node.props, {"href": "www.google.com"})