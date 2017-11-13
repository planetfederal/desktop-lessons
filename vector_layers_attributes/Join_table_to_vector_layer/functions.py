from lessons.utils import layerFromName

# Functions

# EndCheck Function

def fieldExists(layername, string):
    """
    Check if a layer has a field which name contains the specified string
    The layer should be of the vector type and be loaded into project.
    :param layername: Layer's name as visible in the layers panel
    :param string: string of text

    :return: Boolean
    """

    layer = layerFromName(layername)
    if layer is None:
        return False

    for field in layer.pendingFields():
        if string in field.name():
            return True

    return False