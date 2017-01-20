# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
from lessons.lesson import Lesson, Step
from lessons.utils import *
from qgis.utils import iface
from lessons import addLessonModule

def isLayerActive():
    layer = iface.activeLayer()
    return layer is not None and layer.name() == "Downtown streets"

def setActiveLayer():
    layer = layerFromName("Downtown streets")
    iface.setActiveLayer(layer)

# Lesson description

lesson = Lesson("Vector categorized symbols", "Layer styling", "00_lesson.html")

# Steps

lesson.addStep("Set 'Downtown streets' layer as active layer", "01_activelayer.html",
               function = setActiveLayer, endcheck = isLayerActive, steptype = Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Configure categorized Symbol", "03_set_categories.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "04_set_categories_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Change categories symbol", "05_change_style.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "06_change_style_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Combine two fields in categorized Symbol", "07_add_oneway.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "08_add_oneway_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Pre-process values to use in categories", "09_reduce_classes.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "10_reduce_classes_results.html", steptype=Step.MANUALSTEP)


# Suggested lessons

lesson.addNextLesson("Layer styling", "Vector graduated symbols")