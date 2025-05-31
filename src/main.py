import sys
from pages import generate_pages_recursive
from file_handling import copy_static_to_public

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
        
    print(f"Basepath: {basepath}")
    
    print("Copying static files to public directory...")
    copy_static_to_public()
    
    print("Generating content in public directory...")
    generate_pages_recursive("content", "template.html", "docs", basepath)
    

if __name__  == "__main__":
    main()
    