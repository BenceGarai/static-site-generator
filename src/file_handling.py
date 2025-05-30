import os, shutil


def copy_static_to_public():
    public_path = "./public"
    static_path = "./static"
    create_public(public_path)
    
    if os.path.exists(static_path) == False:
        raise ValueError(f"Incorrect static path: {static_path}")
    copy_recursively(static_path, public_path)

        
def create_public(public_path):
    if os.path.exists(public_path):
        print("Public exists, removing and creating folder.")
        shutil.rmtree(public_path)
        os.mkdir(public_path)
    else:
        print("Creating missing public directory")
        os.mkdir(public_path)


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