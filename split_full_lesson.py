import os
import re
import sys


def main ():

    # Get file path from first argument passed in command line
    fl_path = sys.argv[1]
    folder = os.path.dirname(fl_path)
    s_file = None
    s_list= []
    s_number = 0
    with open(fl_path) as full_lesson:
        for line in full_lesson:

            # Patterns
            l = re.match('#\s(.*)', line) # lesson title pattern
            s = re.match('##\s(.*)', line) # step title pattern

            if l:
                l_title = (l.group(0))[2:]
                next(full_lesson) #skip empty line after heading

            # Get step title from markdown heading 2
            elif s:
                s_number += 1
                s_title = (s.group(0))[3:]
                s_file_name = '{0:02d}'.format(s_number) + '_' + \
                              s_title.replace(' ', '_').lower() + '.md'
                s_list.append((s_title, s_file_name))

                # Close description file from previous step
                if s_file != None:
                    s_file.close()

                s_file = open(os.path.join(folder, s_file_name), 'w')


            # Get step description
            else:
                s_file.write(line)
                #Write to opened file

        s_file.close()

if __name__ == '__main__':
    main()