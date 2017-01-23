import os
import zipfile
import shutil
import re

def main ():
    exclude = [".git"]
    folder = os.path.dirname(os.path.realpath(__file__))
    for name in os.listdir(folder):             
        if name not in exclude:             
            fullpath = os.path.join(folder, name)
            if os.path.isdir(fullpath):          
                lessons = []
                for subfolder in os.listdir(fullpath):
                    if os.path.isdir(os.path.join(fullpath, subfolder)) and not subfolder.startswith("_"):
                        lessons.append(subfolder.replace("_", " "))
                manifestFile = os.path.join(fullpath, "lesson.manifest")
                with open(manifestFile) as f:
                    manifest = f.read()
                manifest = re.sub(r"(<lessons_list>).*?(</lessons_list>)", r"\1%s\2" % ",".join(lessons), manifest)
                with open(manifestFile, "w") as f:
                    f.write(manifest)
                shutil.make_archive(os.path.join(folder, name), "zip", fullpath)

if __name__ == '__main__':
    main()