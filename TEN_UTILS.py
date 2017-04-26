import rhinoscriptsyntax as rs
import scriptcontext
from scriptcontext import doc

def renameLay(layerName, newLayerName):
    matchingLayers = [layer for layer in doc.Layers if layer.FullPath == layerName]
    layerToRename = None
    if len(matchingLayers) == 0:
        print "Layer \"{0}\" does not exist.".format(layerName)
        return
    if len(matchingLayers) == 1:
        layerToRename = matchingLayers[0]
    elif len(matchingLayers) > 1:
        i = 0;
        for layer in matchingLayers:
            print "({0}) {1}".format(
                i+1, matchingLayers[i].FullPath.replace("::", "->"))
            i += 1

        selectedLayer = rs.GetInteger(
            "which layer?", -1, 1, len(matchingLayers))
        if selectedLayer == None:
            return
        layerToRename = matchingLayers[selectedLayer - 1]

    #layerName = rs.GetString("New layer name")
    layerToRename.Name = newLayerName
    layerToRename.CommitChanges()
    return
def translateLay(origLayer):
    print origLayer
    strArray = []
    strArray = origLayer.split("::")
    modLayer = ""
    for line in strArray:
        #REMOVES THE ROOT LAYER NAME FROM NAME
       
        if line == "MAKE_2D":
            modLayer = ""
        else:
            if line == "30_AR":
                line = "A"
            modLine = line.replace("_", "-")
            modLayer = modLayer + modLine + "-"
    modLayer = modLayer[:-1]
    print modLayer
    
    return modLayer
if __name__=="__main__":
    layer1 = rs.GetLayer("Select Layer")
    oldName = layer1
    newName = translateLay(layer1)
    renameLay(str(oldName), newName)
    objs = scriptcontext.doc.Objects.FindByLayer(newName)
    rs.SelectObjects(objs)
    savePath = rs.SaveFileName("Save", "Autocad (*.dwg)|*.dwg||")
    rs.Command('! _-Export ' + str(savePath) + ' _Enter')