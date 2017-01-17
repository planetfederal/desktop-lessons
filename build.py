import os
import zipfile
import shutil

def main ():
    exclude = [".git"]
    folder = os.path.dirname(os.path.realpath(__file__))
    for name in os.listdir(folder):
        if name not in exclude:
            fullpath = os.path.join(folder, name)
            if os.path.isdir(fullpath):          
                shutil.make_archive(os.path.join(folder, name), "zip", fullpath)

if __name__ == '__main__':
    main()