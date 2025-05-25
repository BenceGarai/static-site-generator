import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    

    def test_not_eq(self):
        node = TextNode("This is a txt node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    
    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    
    def test_empty_link(self):
        expected_node = TextNode("This is a link type with no link provided", TextType.LINK, None)
        node_to_compare = TextNode("This is a link type with no link provided", TextType.LINK)
        self.assertEqual(expected_node, node_to_compare)
        

    def test_incorrect_text_type(self):
        with self.assertRaises(AttributeError):
            node = TextNode("This is a wrong node", TextType.WRONG)
    

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node))


if __name__ == "__main__":
    unittest.main()