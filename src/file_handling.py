import os, shutil


def copy_static(src_path, dest_path):
    create_dest_dir(dest_path)
    
    if os.path.exists(src_path) == False:
        raise ValueError(f"Incorrect static path: {src_path}")
    copy_recursively(src_path, dest_path)

        
def create_dest_dir(dest_path):
    if os.path.exists(dest_path):
        print("Public exists, removing and creating folder.")
        shutil.rmtree(dest_path)
        os.mkdir(dest_path)
    else:
        print("Creating missing public directory")
        os.mkdir(dest_path)


def copy_recursively(path, destination):
    if os.path.isfile(path):
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copy(path, destination)
        return
    if os.path.exists(destination) == False and os.path.isfile(path) == False:
        os.makedirs(destination, exist_ok=True)
        
    file_list = os.listdir(path)
    
    for file in file_list:
        path_to_check = os.path.join(path, file)
        updated_destination = os.path.join(destination, file)
        
        print("Current path:", path_to_check)
        copy_recursively(path_to_check, updated_destination)