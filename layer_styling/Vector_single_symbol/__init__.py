from lessons.lesson import Lesson, Step
from lessons.utils import *
from qgis.utils import iface
from lessons import addLessonModule

# Lesson's description

lesson = Lesson ("Vector Single Symbol", "Layer styling", "00_lesson.html")


# Steps

lesson.addStep("Introduction", "01_active_layer.md", function=lambda: setActiveLayer("Raleigh_Downtown"),
               endcheck=lambda: layerActive("Raleigh_Downtown"), steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.md")

lesson.addStep("Change layer's symbol", "03_change_simple_fill_settings.md", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm symbol's changes", "04_simple_fill_results.md", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.md")

lesson.addStep("Add Line pattern fill", "05_add_line_pattern.md", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm final result", "06_final_results.md", steptype=Step.MANUALSTEP)

# Suggested lessons

lesson.addNextLesson("Layer styling", "Vector categorized symbols")