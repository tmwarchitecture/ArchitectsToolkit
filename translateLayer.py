import rhinoscriptsyntax as rs

def translateColor(layer, colorString):
    if len(colorString)>1:
        newColor = (int(colorString.split("-")[0]),int(colorString.split("-")[1]),int(colorString.split("-")[2]))
    else:
        newColor = rs.LayerColor(layer)
    return newColor

def translateLayer(layer):
    """
    translates from Rhino Name to CAD Name
    input: one layer
    returns: new layer name
    """
    rhinoLayerFilePath = "C:\\Users\\Tim\\Desktop\\temp\\RhinoLayersV2.csv"
    #Read the CSV
    file = open(rhinoLayerFilePath, "r")
    contents = file.readlines()
    file.close()
    
    #Variables
    CategoryCol = 1
    RhinoLayerCol = 2
    CADNameCol = 9
    CADColorCol = 10
    CADLineweightCol = 11
    found = False
    layerShort = rs.LayerName(layer, False)
    newLayerName = ""
    
    #Check the CSV
    for row in contents:
        rowParts = row.split(",")
        if row.split(",")[RhinoLayerCol]==str(layerShort): #if layer name exists in CSV
            
            CADName = row.split(",")[CADNameCol] 
            CADColor = translateColor(layer, row.split(",")[CADColorCol])
            CADLineweight = row.split(",")[CADLineweightCol]
            
            #if Rhino name found but no CAD name associated with it
            if not CADName: 
                CADName = "A-RHINO-"+layerShort
                newLayerName = CADName
            if len(CADLineweight)<2:
                CADLineweight = 0
            
            #Check if layer already exists.
            parent = rs.ParentLayer(layer)
            existLayers = rs.LayerChildren(parent)
            isExisting = False
            
            for existLayer in existLayers:
                #if new name already exists as a layer
                if rs.LayerName(existLayer, False) == CADName: 
                    layersObjs = rs.ObjectsByLayer(layer)
                    for layersObj in layersObjs:
                        rs.ObjectLayer(layersObj, existLayer)
                    rs.DeleteLayer(layer)
                    newLayerName = rs.LayerName(existLayer, False)
                    print "Layer {} merged with existing layer {}.".format(layerShort, rs.LayerName(layer, False))
                    isExisting = True
                    break
            
            #if layer does not already exist
            if isExisting == False:
                rs.LayerColor(layer, CADColor)
                rs.LayerPrintWidth(layer, float(CADLineweight))
                newLayerName = CADName
                rs.RenameLayer(layer, CADName)
                print "Layer {} changed to layer {}.".format(layerShort,CADName)
            
            found = True
            break
    if not found:
        layerShort = rs.LayerName(layer, False)
        CADName = "A-RHINO-"+layerShort
        newLayerName = CADName
        rs.RenameLayer(layer, CADName)
        print "Layer {} has no matching CAD layer.".format(layerShort)
        return newLayerName
    
    return newLayerName

def main():
    layers = rs.GetLayers("Select Layers to translate to CAD layer names")
    rs.EnableRedraw(False)
    if layers is None:
        return
    for layer in layers:
        translateLayer(layer)
    rs.EnableRedraw(True)

if __name__ == "__main__":
    main()