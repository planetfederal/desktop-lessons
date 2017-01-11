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
    return layer is not None and layer.name() == "landsat_8_sample"

def setActiveLayer():
    layer = layerFromName("landsat_8_sample")
    iface.setActiveLayer(layer)

# Lesson description

lesson = Lesson("Raster multiband styling", "Layer styling", "00_lesson.html")

# Steps

lesson.addStep("Set 'landsat_8_sample' layer as active layer", "01_activelayer.html",
               function = setActiveLayer, endcheck = isLayerActive, steptype = Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Set layer style to Singleband pseudocolor", "03_set_432_natural_color.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "04_set_432_natural_color_results.html", steptype=Step.MANUALSTEP)

lesson.addMenuClickStep("Layer/Properties...", "02_open_properties.html")

lesson.addStep("Set better legend values", "05_set_543_infrared_color.html", steptype=Step.MANUALSTEP)

lesson.addStep("Confirm results", "06_set_543_infrared_color_results.html", steptype=Step.MANUALSTEP)

# Suggested lessons

lesson.addNextLesson("Layer styling", "Raster multiband styling")