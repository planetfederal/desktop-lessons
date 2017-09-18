from lessons.utils import layerFromName

# Functions

# EndCheck Function

def isLayerEditable(*args):
    """Returns True if layer with given name is in editable mode.
    NOTE: layer should be of the vector type and be loaded into project.
    """
    layer = layerFromName(args[0])
    return layer is not None and layer.isEditable()
