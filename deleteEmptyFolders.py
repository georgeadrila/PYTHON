import os

# Define the directory to start the search from
root_dir = 'C:/Users\George Adrian/Desktop/images'

# Define a function to check if a directory is empty
def is_empty(dir):
    return len(os.listdir(dir)) == 0

# Define a function to delete empty directories recursively
def delete_empty_directories(dir):
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in dirs:
            dir_path = os.path.join(root, name)
            if is_empty(dir_path):
                print(f"Deleting empty directory: {dir_path}")
                os.rmdir(dir_path)

# Call the delete_empty_directories() function
delete_empty_directories(root_dir)
