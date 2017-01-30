# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
from lessons.lesson import Lesson, Step
from lessons.utils import setActiveLayer, layerActive
from qgis.utils import iface
from lessons import addLessonModule

def isLayerActive():
    layer = iface.activeLayer()
    return layer is not None and layer.name() == "dem25"

def setActiveLayer():
    layer = layerFromName("dem25")
    iface.setActiveLayer(layer)

# Lesson description
lesson = Lesson("Raster singleband styling", "Layer styling", "00_lesson.html")

# Steps
lesson.addStep("Set 'dem25' layer as active layer", "01_activelayer.html",
               function=lambda: setActiveLayer("dem25"),
               endcheck=lambda: layerActive("dem25"),
               steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Set layer style to Singleband pseudocolor", "03_set_singleband_pseudocolor.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "04_set_singleband_pseudocolor_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Set better legend values", "05_set_better_legend_values.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "06_set_better_legend_values_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Set discrete color interpolation mode", "07_set_discrete_mode.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "08_set_discrete_mode_results.html", steptype=Step.MANUALSTEP)

# Suggested lessons
lesson.addNextLesson("Layer styling", "Raster multiband styling")
