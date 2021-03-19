import os
from shutil import copytree


def copy_folder():
    dir = "my_project"
    folder = "templates"

    for root, dirs, files in os.walk(dir):
        if root.find(folder) > 0 and len(files) == 0:
            copytree(os.path.join(root), folder, dirs_exist_ok=True)


if __name__ == '__main__':
    copy_folder()
