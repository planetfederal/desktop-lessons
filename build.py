import os
import zipfile

def main ():
    exclude = [".git"]
    folder = os.path.dirname(os.path.realpath(__file__))
    print folder
    for name in os.listdir(folder):
        if name not in exclude:
            fullpath = os.path.join(folder, name)
            if os.path.isdir(fullpath):          
                zipf = zipfile.ZipFile(name + '.zip', 'w', zipfile.ZIP_DEFLATED)
                for root, dirs, files in os.walk(fullpath):
                    for f in files:
                        zipf.write(os.path.join(root, f), os.path.join(name, f))
                zipf.close()                    



if __name__ == '__main__':
    main()