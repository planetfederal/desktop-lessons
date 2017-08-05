# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
from lessons.lesson import Step, Lesson
from lessons.utils import layerExists, layerFromName
from qgis.utils import iface

# EndCheck functions

lesson = Lesson("01. Load ArcGIS REST services layers",
                "Third party integration",
                "lesson.html")

lesson.addStep("Introduction",
               "01_introduction.md",
               steptype=Step.MANUALSTEP)
lesson.addMenuClickStep("Layers/Add Layer/Add ArcGIS MapServer",
                        "02_open_arcgis_add_mapserver_layer.md")
lesson.addStep("Setup a ArcGISMapServer connection",
               "03_setup_connection.md",
               endcheck=lambda: layerExists("States", "raster"),
               steptype=Step.MANUALSTEP)
lesson.addStep("Inspect ArcGISMapServer layer",
               "04_inspect_ArcGisMapServer_layer.md",
               steptype=Step.MANUALSTEP)
lesson.addStep("Open Browser Panel",
               "05_open_browser_panel.md",
               steptype=Step.MANUALSTEP)
lesson.addStep("Add ArcGISFeatureServer connection",
               "06_Add_a_connection_in_browser.md",
               steptype=Step.MANUALSTEP)
lesson.addStep("Load Layer using Browser",
               "07_load_layer_in_canvas_from_browser.md",
               endcheck=lambda: layerExists("Shelters", "vector"),
               steptype=Step.MANUALSTEP)
lesson.addStep("Inspect ArcGISFeatureServer layer",
               "08_inspect_arcgisFeatureServer_layer.md",
               steptype=Step.MANUALSTEP)

# lesson.addNextLesson("Image Discovery plugin", "02. Search and Download
# Images")
