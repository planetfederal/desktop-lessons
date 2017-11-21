# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
from lessons.lesson import Lesson, Step
from qgis.utils import iface
from lessons import addLessonModule

# Lesson description
lesson = Lesson("09. Manage multiple styles in a layer", "Layer styling",
                "00_lesson.html")

# Steps
lesson.addStep("Introduction", "01_intro.html", steptype=Step.MANUALSTEP)

lesson.addStep("Rename current style", "02_rename_existing_style.html", steptype=Step.MANUALSTEP)

lesson.addStep("Create new style", "03_create_new_style.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "04_open_properties.html")

lesson.addStep("Change new style settings", "05_create_occupied_ratio_style.html", steptype=Step.MANUALSTEP)

lesson.addStep("Go back to previous style", "06_revert_to_population_density.html", steptype=Step.MANUALSTEP)

# Suggested lessons
lesson.addNextLesson("Layer styling", "10. Using data-defined properties")
