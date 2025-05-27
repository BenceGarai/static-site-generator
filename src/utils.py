from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_node_text = node.text.split(delimiter)
            
            if len(split_node_text) % 2 == 0:
                raise Exception("Invalid markdown syntax: no closing delimiter")
            
            for index, text in enumerate(split_node_text):
                if len(text) == 0:
                    continue
                if index % 2 == 0:
                    # even index
                    new_nodes.append(TextNode(text, TextType.TEXT, None))
                else:
                    # odd index
                    new_nodes.append(TextNode(text, text_type, None))
        else:
            new_nodes.append(node)
            
    return new_nodes
