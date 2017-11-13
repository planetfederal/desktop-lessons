from lessons.utils import layerFromName

# Functions

# EndCheck Function

def checkJoinExists (layername, fieldname, targetlayer, targetfield):
    """
    Returns True if vector layer has a join with a
    target layer using the specified field and target field
    :param layername: vector layer name
    :param fieldname: join field name
    :param targetlayer: target vector layer name
    :param targetfield: target join field name
    :return: Boolean
    """

    layer = layerFromName(layername)
    tlayer = layerFromName(targetlayer)

    # check if layers exist
    if layer is None or tlayer is None:
        return False

    # check if join fields exist
    if fieldname not in [f.name() for f in layer.pendingFields()] or \
       targetfield not in [f.name() for f in tlayer.pendingFields()]:
        return False

    join_settings = (tlayer.id(), unicode(targetfield), unicode(fieldname))

    for j in layer.vectorJoins():
        if (j.joinLayerId, j.joinFieldName, j.targetFieldName) == join_settings:
            return True

    return False