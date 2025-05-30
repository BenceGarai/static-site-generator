from pages import generate_page
from file_handling import copy_static_to_public

def main():
    print("Calling copy function")
    copy_static_to_public()
    print("Copy complete")
    generate_page("content/index.md", "template.html", "public/index.html")
    

if __name__  == "__main__":
    main()
    