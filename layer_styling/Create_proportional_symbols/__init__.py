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
lesson = Lesson("Create Proportional Symbols", "Layer styling", "00_lesson.html")

# Steps
lesson.addStep("Set 'Wake_Public_Schools' layer as active layer", "01_activelayer.html",
               function=lambda: setActiveLayer("Wake_Public_Schools"),
               endcheck=lambda: layerActive("Wake_Public_Schools"),
               steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Use size assistant to set symbols", "03_set_proportional_symbols.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "04_proportional_size_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Change size expression", "05_view_expression.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm final results", "06_view_expression_results.html", steptype=Step.MANUALSTEP)

# Suggested lessons
lesson.addNextLesson("Layer styling", "Raster singleband styling")
