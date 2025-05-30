from htmlnode import HTMLNode
from textnode import *
from leafnode import LeafNode
from parentnode import ParentNode
from utils import copy_static_to_public

def main():
    print("Calling copy function")
    copy_static_to_public()
    print("Copy complete")
    

if __name__  == "__main__":
    main()
    