from htmlnode import HTMLNode
from textnode import *

def main():
    test_props = {"href": "https://www.google.com",
                      "target": "_blank"}

    test_html = HTMLNode("p", "This is a paragraph", None, test_props)
    print(test_html.props_to_html())
    print(test_html)

if __name__  == "__main__":
    main()
    