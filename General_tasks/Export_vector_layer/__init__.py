# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
from lessons.lesson import Lesson, Step
from lessons.utils import setActiveLayer, layerActive
from qgis.utils import iface
from lessons import addLessonModule


lesson = Lesson("01. Export vector layer", "General tasks", "lesson.html")
lesson.addStep("Set 'points' layer as active layer", "activelayer.html",
               function=lambda: setActiveLayer("points"),
               endcheck=lambda: layerActive("points"),
               steptype=Step.MANUALSTEP)
lesson.addMenuClickStep("Layer/Save As...", name="Click on 'Layer > Save As...' menu item.")
lesson.addStep("Save layer to new format", "saveas.html", steptype=Step.MANUALSTEP)
lesson.addNextLesson("General tasks", "02. Export raster layer")

