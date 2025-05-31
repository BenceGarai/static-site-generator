from pages import generate_pages_recursive
from file_handling import copy_static_to_public

def main():
    copy_static_to_public()
    generate_pages_recursive("content", "template.html", "public")
    

if __name__  == "__main__":
    main()
    