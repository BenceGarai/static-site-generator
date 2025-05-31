from pages import generate_pages_recursive
from file_handling import copy_static_to_public

def main():
    print("Copying static files to public directory...")
    copy_static_to_public()
    
    print("Generating content in public directory...")
    generate_pages_recursive("content", "template.html", "public")
    

if __name__  == "__main__":
    main()
    