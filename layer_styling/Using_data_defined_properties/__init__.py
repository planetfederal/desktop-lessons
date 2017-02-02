from lessons.lesson import Lesson, Step
from lessons.utils import *
from qgis.utils import iface
from lessons import addLessonModule

# Lesson's description

lesson = Lesson ("Using data-defined properties", "Layer styling", "00_lesson.html")


# Steps

lesson.addStep("Introduction", "01_intro.md", steptype=Step.MANUALSTEP)

lesson.addStep("Make 'Wake_MajorRoads' active", "02_active_layer.md", function=lambda: setActiveLayer("Wake_MajorRoads"),
               endcheck=lambda: layerActive("Wake_MajorRoads"), steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "03_open_properties.md")

lesson.addStep("Set data-override to Pen Width option", "04_set_overrride_settings.md", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm data-override results", "05_override_results.md", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "03_open_properties.md")

lesson.addStep("Set an expression for Pen Width option", "06_set_overrride_expression.md", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm expression results", "07_set_expression_results.md", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "03_open_properties.md")

lesson.addStep("Set an expression for color option", "08_intersect_expression.md", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm final results", "09_intersect_expression_results.md", steptype=Step.MANUALSTEP)

# Suggested lessons

lesson.addNextLesson("Layer styling", "Create Proportional Symbols")