# desktop-lessons

Lessons for the QGIS Lessons plugin.

Lesson are grouped by folder. Each folder contains a set of lessons, all of them meant to be distributed together. Individual lessons should be stored as subfolders of the parent set folder.

Type ``python build.py`` to run the Python task that generates distributables lessons sets. It will create a zip file for each of the lesson sets. Those can later be installed by the QGIS Lessons plugin using the ``lessons.installLessonsfromZipFile()`` method
