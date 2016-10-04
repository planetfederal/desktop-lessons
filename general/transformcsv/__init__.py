from lessons.lesson import Lesson, Step
from lessons.utils import *
from qgis.utils import iface
from lessons import addLessonModule

lesson = Lesson ("Transform X and Y CSV table into a point vector layer",
                 "General tasks", "lesson.html")

lesson.addMenuClickStep('Layer/Add Layer/Add Delimited Text Layer...')

lesson.addStep('Configure importing settings', 'delimited_test_settings.html')

lesson.addStep('Set layer as active layer', 'set_active_layer.html')

lesson.addMenuClickStep('Layer/Save As...')

lesson.addStep('Save the file as GeoPackage', 'save_as_geopackage.html')
