import rhinoscriptsyntax as rs

def mergeLayers(layA, layB):
    """
    layA is kept, layB is deleted
    input: (layA, layB) each is a layer, the top parent in a tree to merge with another.
    returns: None
    """
    rs.EnableRedraw(False)
    Alayers = rs.LayerChildren(layA)
    Blayers = rs.LayerChildren(layB)
    AlayersShort = []
    BlayersShort = []
    for Alayer in Alayers:
        AlayersShort.append(rs.LayerName(Alayer, False))
    for Blayer in Blayers:
        BlayersShort.append(rs.LayerName(Blayer, False))
    uniqueLayers = list(set(BlayersShort) - set(AlayersShort))
    #move unique layers
    for uniqueLayer in uniqueLayers:
        rs.ParentLayer(uniqueLayer, layA)
    
    #get duplicate name layers
    duppedLayers = list(set(BlayersShort) - set(uniqueLayers))
    
    #move objects to layA twin
    for duppedLayer in duppedLayers:
        newParent = layA + "::" + duppedLayer
        duppedObjs = rs.ObjectsByLayer(layB + "::" + duppedLayer)
        for duppedObj in duppedObjs:
            rs.ObjectLayer(duppedObj, newParent)
        #if it has children, recursively move them
        if rs.LayerChildCount(layB + "::" + duppedLayer)>0:
            mergeLayers(layA + "::" + duppedLayer, layB + "::" + duppedLayer)
        else:
            rs.DeleteLayer(layB + "::" + duppedLayer)
            rs.DeleteLayer(layB)
    rs.EnableRedraw(True)
    return None

def main():
    layerA = rs.GetLayer("Layer Tree to Keep")
    layerB = rs.GetLayer("Layer Tree to Merge")
    mergeLayers(layerA, layerB)
    return

if __name__ == "__main__":
    main()