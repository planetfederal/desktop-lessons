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
lesson = Lesson("Vector graduated symbols", "Layer styling", "00_lesson.html")

# Steps
lesson.addStep("Set 'Wake BlockGroup 2010' layer as active layer", "01_activelayer.html",
               function=lambda: setActiveLayer("Wake BlockGroup 2010"),
               endcheck=lambda: layerActive("Wake BlockGroup 2010"),
               steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Configure graduated Symbol", "03_set_graduated.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "04_set_graduated_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Use population density", "05_add_area.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "06_add_area_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Convert sq ft to sq miles", "07_convert_to_miles.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "08_convert_to_miles_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Change classification method", "09_change_method.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "10_change_method_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Convert population to thousands", "11_to_thousands.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "12_to_thousands_results.html", steptype=Step.MANUALSTEP)

# Suggested lessons
lesson.addNextLesson("Layer styling", "Vector rule-based symbols")
