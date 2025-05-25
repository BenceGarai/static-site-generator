from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    
    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid Parent: No tag")
        if self.children is None:
            raise ValueError("invalid Parent: No children")

        result = ""
        for child in self.children:
            if isinstance(child, LeafNode):
                result += child.to_html()
            else:
                # Same logic for now
                result += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'