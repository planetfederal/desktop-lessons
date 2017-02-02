# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
from lessons.lesson import Lesson, Step
from lessons.utils import setActiveLayer, layerActive
from qgis.utils import iface
from lessons import addLessonModule

lesson = Lesson("Define vector layer CRS", "General tasks", "lesson.html")

lesson.addStep("Set 'Wake_BlockGroup_2010' layer as active layer", "activelayer.html",
               function=lambda: setActiveLayer("Wake_BlockGroup_2010"),
               endcheck=lambda: layerActive("Wake_BlockGroup_2010"),
               steptype=Step.MANUALSTEP)
lesson.addMenuClickStep("Layer/Set CRS of Layer(s)")
lesson.addStep("Set the layer's correct CRS", "setcrs.html", steptype=Step.MANUALSTEP)
lesson.addMenuClickStep("Vector/Data Management Tools/Define Current Projection...", "gotodefineprojection.html")
lesson.addStep("Define new CRS to file", "defineprojection.html", steptype=Step.MANUALSTEP)
lesson.addNextLesson("General tasks", "Reproject vector layer")
