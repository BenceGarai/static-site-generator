from textnode import TextNode, TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node: TextNode):
  # raise excepction of TextType does not match with existing ones
  if not isinstance(text_node.text_type, TextType):
      raise ValueError("Invalid TextType")
  
  # handle each type of TextType in TextNode
  match text_node.text_type:
      case TextType.TEXT:
          return LeafNode(None, text_node.text, None)
      case TextType.BOLD:
          return LeafNode("b", text_node.text, None)
      case TextType.ITALIC:
          return LeafNode("i", text_node.text, None)
      case TextType.CODE:
          return LeafNode("code", text_node.text, None)
      case TextType.LINK:
          return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
      case TextType.IMAGE:
          return LeafNode("img", "", {"src": f"{text_node.url}", "alt": "alttext"})


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    
    for index, block in enumerate(blocks):
        blocks[index] = block.strip()
        if len(block) == 0:
            blocks.pop(block)
        
    return blocks
