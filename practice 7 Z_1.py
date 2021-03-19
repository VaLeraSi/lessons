import os

folder = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def make_folders(f_folder):
    for i, j in f_folder.items():
        if not os.path.exists(i):
            for a in range(len(j)):
                os.makedirs(os.path.join(i, j[a]))


make_folders(folder)
