import os

from lessons.lesson import Lesson, Step
from qgis.utils import iface
from lessons import addLessonModule
from lessons.utils import copyLessonData


# Copy dataset to the user's folder
def copyTable():
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Setting_layer_default_style/data", "Wake_BlockGroup_2010.zip")
    copyLessonData(filepath, os.path.basename(os.path.dirname(__file__)))


# Lesson's description
lesson = Lesson ("08. Setting layer's default style", "Layer styling",
                 "00_lesson.html")

# Steps
lesson.addStep("Copy data", "Copy data", copyTable)

lesson.addStep('Introduction', '01_intro.html', steptype=Step.MANUALSTEP)

lesson.addMenuClickStep('Layer/Add Layer/Add Vector Layer...')

lesson.addStep('Load example dataset', '02_select_dataset_file.html', steptype=Step.MANUALSTEP)

lesson.addMenuClickStep('Layer/Properties...', '03_open_properties.html')

lesson.addStep('Change layer style', '04_change_settings.html', steptype=Step.MANUALSTEP)

lesson.addMenuClickStep('Layer/Add Layer/Add Vector Layer...', '05_open_dataset_again.html')

lesson.addStep('Load example dataset', '02_select_dataset_file.html', steptype=Step.MANUALSTEP)

lesson.addStep('Conclusion', '06_conclusion.html', steptype=Step.MANUALSTEP)

# Suggested lessons
lesson.addNextLesson("Layer styling", "09. Manage multiple styles in a layer")
