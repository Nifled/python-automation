# Script reads every file in directory with specified path

import os


def main():

    path = '/Users/nifled/Downloads/NUEVO'

    for root, subdirs, files in os.walk(path):
        for file in os.listdir(root):
            file_path = os.path.join(root, file)
            if os.path.isdir(file_path):
                pass
            else:
                parent_dir = file_path.split('/')[-2]
                print(parent_dir, file_path.split('/')[-1].split('.')[0])


if __name__ == '__main__':
    main()
