import unittest
from utils import *
from textnode import TextType, TextNode


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        matches = "[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None)]"
        self.assertEqual(repr(split_nodes), matches)
        
        
    def test_two_code_blocks(self):
        node = TextNode("This is text with a `code block` word and another `code block` word", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        matches = "[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word and another , text, None), TextNode(code block, code, None), TextNode( word, text, None)]"
        self.assertEqual(repr(split_nodes), matches)

    
    def test_no_closing_delimiter(self):
        node = TextNode("This is text with a `code block` word and another `code block word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)
            
    
    def test_delimiter_not_found(self):
        node = TextNode("This is text with no delimiter in it", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        matches = "[TextNode(This is text with no delimiter in it, text, None)]"
        self.assertEqual(repr(split_nodes), matches)
        
            
    def test_delimiter_at_beginning(self):
        node = TextNode("`code block` there is a delimiter in the beginning!", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        matches = "[TextNode(code block, code, None), TextNode( there is a delimiter in the beginning!, text, None)]"
        self.assertEqual(repr(split_nodes), matches)
        
    
    def test_delimiter_at_end(self):
        node = TextNode("There is a delimiter at the end, `code block`", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        matches = "[TextNode(There is a delimiter at the end, , text, None), TextNode(code block, code, None)]"
        self.assertEqual(repr(split_nodes), matches)
        

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_markdown_images(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
