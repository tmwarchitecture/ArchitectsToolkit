#AR_GRID

import rhinoscriptsyntax as rs
import opUtil as op
def TEN_GRID_TEXT(optLayID):
    subLayName = "Grids"
    layName = "TEXT"
    layColor = [255,255,0]
    layMatIndex = -1
    printColor = [50,50,50]
    printWidth = .18
    
    #ADD SUB-LAYER
    subLayID = rs.AddLayer(subLayName, [125,125,255], parent = optLayID)
    
    #ADD OBJECT LAYER
    lay = rs.AddLayer(layName, layColor, parent = subLayID)
    
    #CHANGE CURRENT LAYER TO NEW LAYER
    rs.CurrentLayer(lay)
    
    #CHANGE LAYER MATERIAL
    #rs.LayerMaterialIndex(lay, layMatIndex)
    
    #CHANGE LAYER PRINT ATTRIBUTES
    rs.LayerPrintColor(lay, printColor)
    rs.LayerPrintWidth(lay, printWidth)
    
    return None
def TEN_GRID_GRID(optLayID):
    subLayName = "Grids"
    layName = "GRID"
    layColor = [150,150,150]
    layMatIndex = -1
    printColor = [50,50,50]
    printWidth = .18
    
    #ADD SUB-LAYER
    subLayID = rs.AddLayer(subLayName, [125,125,255], parent = optLayID)
    
    #ADD OBJECT LAYER
    lay = rs.AddLayer(layName, layColor, parent = subLayID)
    
    rs.CurrentLayer(lay)
    #rs.LayerMaterialIndex(lay, layMatIndex)
    rs.LayerPrintColor(lay, printColor)
    rs.LayerPrintWidth(lay, printWidth)
    return None
def TEN_GRID_DIM(optLayID):
    subLayName = "Grids"
    layName = "DIM"
    layColor = [150,150,150]
    layMatIndex = -1
    printColor = [50,50,50]
    printWidth = .18
    
    #ADD SUB-LAYER
    subLayID = rs.AddLayer(subLayName, [125,125,255], parent = optLayID)
    
    #ADD OBJECT LAYER
    lay = rs.AddLayer(layName, layColor, parent = subLayID)
    
    rs.CurrentLayer(lay)
    #rs.LayerMaterialIndex(lay, layMatIndex)
    rs.LayerPrintColor(lay, printColor)
    rs.LayerPrintWidth(lay, printWidth)
    return None
def main():
    layToAdd = rs.GetInteger("")
    
    layer = rs.CurrentLayer()
    optNum = op.getLayerOpNum(layer)
    if optNum is None:
        return
    if (len(str(optNum))<2):
        optNum = "0" + str(optNum)
    optName = "OP_" + str(optNum)
    
    #ADD BASE LAYER
    baseLay = "30_AR"
    baseLayID = rs.AddLayer(baseLay, [50,50,50])
    
    #ADD OPTION LAYER
    optLayID = rs.AddLayer(optName, [50,50,50], parent = baseLayID)
    
    #ADD AR_WALL_EXTL_GLAZ LAYER
    if (layToAdd == 1 or layToAdd == 0):
        TEN_GRID_TEXT(optLayID)
    if (layToAdd == 2 or layToAdd == 0):
        TEN_GRID_GRID(optLayID)
    if (layToAdd == 3 or layToAdd == 0):
        TEN_GRID_DIM(optLayID)
    return None

if __name__=="__main__":
    rs.EnableRedraw(False)
    main()
    rs.EnableRedraw(True)