from lessons.utils import layerFromName
from qgis.core import QgsMapLayer, QgsRectangle

# Functions

def selectByRectangle(layername, xmin, ymin, xmax, ymax):
    """
    Select features in rectangle
    :param layername: Layer's name as in the layers panel
    :return: None
    """

    layer = layerFromName(layername)
    if layer is not None and layer.type() == QgsMapLayer.VectorLayer:
        layer.selectByRect(QgsRectangle(xmin, ymin, xmax, ymax))

# EndCheck Function

def isLayerEditable(*args):
    """Returns True if layer with given name is in editable mode.
    NOTE: layer should be of the vector type and be loaded into project.
    """
    layer = layerFromName(args[0])
    return layer is not None and layer.isEditable()

def isLayerSaved(layername):
    """
    Returns True if no changes were made in the layer after the last save
    :param layername: Layer name as in the layers panel
    :return: Boolean
    """

    layer = layerFromName(layername)
    return layer is not None and layer.type() == QgsMapLayer.VectorLayer and \
           not layer.isModified()

def checkFieldValue(layername, field, value):
    """
    Return True if all features have a certain value for a
    particular field. If the layer has selected features, only those will be
    taken in account
    :param layername: Layer's name as in the layers panel
    :param field: Field name
    :param value: value to confirm
    :return: Boolean
    """

    layer = layerFromName(layername)
    if layer is None:
        return False

    if layer.selectedFeatureCount():
        features = layer.selectedFeatures()
    else:
        features = layer.getFeatures()

    for feature in features:
        if feature.attribute(field) != value:
            return False

    return True
