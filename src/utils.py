from textnode import TextType, TextNode
import re


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


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


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        extracted_images = extract_markdown_images(node.text)
        if len(extracted_images) == 0 and len(node.text) != 0:
            new_nodes.append(node)
            continue
        for image_alt, image_link in extracted_images:
            section = node.text.split(f"![{image_alt}]({image_link})", 1)
            if len(section[0]) > 0:
                new_nodes.append(TextNode(section[0], TextType.TEXT, None))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            node.text = section[1]
        if len(node.text) > 0:
            new_nodes.append(TextNode(node.text, TextType.TEXT, None))
    
    return new_nodes
            
    
def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        extracted_links = extract_markdown_links(node.text)
        if len(extracted_links) == 0 and len(node.text) != 0:
            new_nodes.append(node)
            continue
        for link_alt, link_url in extracted_links:
            section = node.text.split(f"[{link_alt}]({link_url})", 1)
            if len(section[0]) > 0:
                new_nodes.append(TextNode(section[0], TextType.TEXT, None))
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
            node.text = section[1]
        if len(node.text) > 0:
            new_nodes.append(TextNode(node.text, TextType.TEXT, None))
    
    return new_nodes



