import rhinoscriptsyntax as rs

def makeRoofPlan(layers):
    """
    make2d from above.
    input: list of layers to make2d
    returns: None
    """
    rs.EnableRedraw(False)
    #Get the objects
    objsRaw = []
    for layer in layers:
        objsRaw.append(rs.ObjectsByLayer(layer))
    objs = [item for sublist in objsRaw for item in sublist]
    
    #Make2d
    rs.SelectObjects(objs)
    rs.Command("-_make2d _D _U _Enter")
    projLines = rs.GetObjects("", preselect = True)
    
    #Get make2d root layer
    make2dRootRaw = rs.ObjectLayer(projLines[0])
    make2dRoot = make2dRootRaw.split("::")[0]
    
    #Rename make2d layers
    root  = rs.AddLayer("60_PLANS")
    roofLay = rs.AddLayer("Roof", parent = root)
    for projLine in projLines:
        linesLayer = rs.ObjectLayer(projLine)
        linesColor = rs.ObjectColor(projLine)
        linesLayerName = rs.LayerName(linesLayer, fullpath = False)
        newLayers = rs.AddLayer(linesLayerName, parent = roofLay, color = linesColor)
        rs.ObjectLayer(projLine,newLayers)
    
    #Delete make2d Layers
    rs.DeleteLayer(make2dRoot)
    rs.EnableRedraw(True)
    return

def main():
    layers = rs.GetLayers("Select layers to make roof plan of")
    if layers is None:
        return
    makeRoofPlan(layers)

main()    