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
lesson = Lesson("Vector rule-based symbols", "Layer styling", "00_lesson.html")

# Steps
lesson.addStep("Introduction", "01_intro.html", steptype=Step.MANUALSTEP)

lesson.addStep("Set 'Buildings' layer as active layer", "02_active_layer.html",
               function=lambda: setActiveLayer("Buildings"),
               endcheck=lambda: layerActive("Buildings"),
               steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "03_open_properties.html")

lesson.addStep("Set the first rule", "04_set_first_rule.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm the results", "05_set_first_rule_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "03_open_properties.html")

lesson.addStep("Set the ELSE rule", "06_set_else_rule.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm the results", "07_set_else_rule_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "03_open_properties.html")

lesson.addStep("Nest existing rules", "08_nest_rules.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm the results", "09_nest_rules_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "03_open_properties.html")

lesson.addStep("Set update rule", "10_set_update_rule.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm the results", "11_set_update_rule_results.html", steptype=Step.MANUALSTEP)

# Suggested lessons
lesson.addNextLesson("Layer styling", "Create Proportional Symbols")
