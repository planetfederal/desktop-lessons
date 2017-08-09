import os
import re
import sys
import yaml

def main ():

    # Get file path from first argument passed in command line
    fl_path = sys.argv[2]
    folder = os.path.dirname(fl_path)
    s_file = None
    s_list= []
    l_structure = {'name': '',
                   'group': '',
                   'description': 'lesson.md',
                   'steps': [],
                   'nextLessons': [{'name': '', 'group': ''}]}
    s_number = 0
    with open(fl_path) as full_lesson:
        for line in full_lesson:

            # Patterns
            l = re.match('#\s(.*)', line) # lesson title pattern
            s = re.match('##\s(.*)', line) # step title pattern
            b = re.match('\n', line) # step title pattern

            if l:
                l_title = (l.group(0))[2:]
                l_structure['name'] = l_title
                s_file = open(os.path.join(folder, 'lesson.md'), 'w+')
                next(full_lesson) # skip empty line after heading

            # Get step title from markdown heading 2
            elif s:
                s_number += 1
                s_title = (s.group(0))[3:]
                s_file_name = '{0:02d}_{1}.md'.format(s_number, s_title.replace(
                    ' ', '_').lower())
                l_structure['steps'].append({'name':l_title,
                                             'description': s_file_name})
                s_list.append((s_title, s_file_name))

                # Close description file from previous step
                if s_file != None:
                    clean_empty_lines(s_file)
                    s_file.close()
                # Open step description file
                s_file = open(os.path.join(folder, s_file_name), 'w+')

                next(full_lesson) # skip empty line after heading

            # Get step description
            else:
                s_file.write(line) #Write to opened file

        s_file.close()

    # Write Lesson's YAML file
    with open(os.path.join(folder, 'lesson.yaml'), 'w')  as yaml_file:
        yaml.dump(l_structure, yaml_file, default_flow_style=False,
                  allow_unicode=True)
    print "Splitting was completed."

def clean_empty_lines(open_file):
    open_file.seek(0, os.SEEK_END)
    pos = open_file.tell() -1
    # Read the file backwords until it finds an non end of line character
    while pos > 0 and open_file.read(1) != '\n':
        pos -= 1
        open_file.seek(pos, os.SEEK_SET)

    if pos > 0:
        open_file.seek(pos, os.SEEK_SET)
        open_file.truncate()

if __name__ == '__main__':
    main()

