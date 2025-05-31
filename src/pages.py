import os
from pathlib import Path
from converters import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if "#" in line:
            stripped_line = line.strip()
            if stripped_line.startswith("#") and len(stripped_line) > 1:
                return stripped_line[1:].strip()
    raise Exception("No h1 found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as file:
        markdown_file = file.read()
    
    with open(template_path, "r") as file:
        template_file = file.read()
    
    html_node = markdown_to_html_node(markdown_file)
    title = extract_title(markdown_file)
    
    html_page = template_file.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", html_node.to_html())
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, "w") as file:
        file.write(html_page)
        

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)