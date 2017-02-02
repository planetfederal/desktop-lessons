# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
from lessons.lesson import Lesson, Step
from lessons.utils import setActiveLayer, layerActive
from qgis.utils import iface
from lessons import addLessonModule


# Lesson description
lesson = Lesson("Labelling vector layers", "Layer styling", "00_lesson.html")

# Steps
lesson.addStep("Set 'Wake_ZIP_Codes' layer as active layer", "01_activelayer.html",
               function=lambda: setActiveLayer("Wake_ZIP_Codes"),
               endcheck=lambda: layerActive("Wake_ZIP_Codes"),
               steptype=Step.MANUALSTEP)
lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Set labels settings for polygons layer", "03_turn_labels_on.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm labels results", "04_label_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Set improved position", "05_improve_label_position.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm position changes", "06_label_position_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "07_open_properties.html")

lesson.addStep("Set labels settings for line layer", "08_line_label_settings.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm labels results", "09_line_settings_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "07_open_properties.html")

lesson.addStep("Activate merge lines option", "10_merge_lines.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm merge lines results", "11_merge_lines_result.html", steptype=Step.MANUALSTEP)

# Suggested lessons
lesson.addNextLesson("Layer styling", "Setting layer's default style")
