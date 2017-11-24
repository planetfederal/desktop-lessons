from lessons.lesson import Lesson, Step
from lessons.utils import *
from qgis.utils import iface
from lessons import addLessonModule

# Lesson's description

lesson = Lesson ("01. Vector Single Symbol", "Layer styling", "00_lesson.html")


# Steps

lesson.addStep("Introduction",
               "01_introduction.md",
               steptype=Step.MANUALSTEP)

lesson.addStep("Set active layer", "02_active_layer.md",
               function=lambda: setActiveLayer("Raleigh_Downtown"),
               endcheck=lambda: layerActive("Raleigh_Downtown"),
               steptype=Step.MANUALSTEP)

lesson.addStep("Open Styling panel", "03_open_styling_panel.md",
               steptype=Step.MANUALSTEP)

lesson.addStep("Change layer's symbol", "04_change_simple_fill_settings.md",
               steptype=Step.MANUALSTEP)

lesson.addStep("Confirm symbol's changes", "05_simple_fill_results.md",
               steptype=Step.MANUALSTEP)

lesson.addStep("Add Line pattern fill", "06_add_line_pattern.md",
               steptype=Step.MANUALSTEP)

lesson.addStep("Confirm final result", "07_final_results.md",
               steptype=Step.MANUALSTEP)

# Suggested lessons

lesson.addNextLesson("Layer styling", "02. Vector categorized symbols")