#AR_CIRC

import rhinoscriptsyntax as rs
import opUtil as op

def TEN_CIRC_STAIR(optLayID):
    subLayName = "Circulation"
    subLayColor = [125,125,255]
    layName = "STAIR"
    layColor = [255,255,100]
    layMatIndex = -1
    printColor = [0,0,0]
    printWidth = .18
    
    #ADD SUB-LAYER
    subLayID = rs.AddLayer(subLayName, subLayColor, parent = optLayID)
    
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
def TEN_CIRC_LIFT(optLayID):
    subLayName = "Circulation"
    subLayColor = [125,125,255]
    layName = "LIFT"
    layColor = [255,255,100]
    layMatIndex = -1
    printColor = [0,0,0]
    printWidth = .18
    
    #ADD SUB-LAYER
    subLayID = rs.AddLayer(subLayName, subLayColor, parent = optLayID)
    
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
def TEN_CIRC_ESCL(optLayID):
    subLayName = "Circulation"
    subLayColor = [125,125,255]
    layName = "ESCL"
    layColor = [255,255,100]
    layMatIndex = -1
    printColor = [0,0,0]
    printWidth = .18
    
    #ADD SUB-LAYER
    subLayID = rs.AddLayer(subLayName, subLayColor, parent = optLayID)
    
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

def main():
    #GET OPTION NUMBER FROM USER
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
    
    #ADD EACH LAYER
    if (layToAdd == 1 or layToAdd == 0):
        TEN_CIRC_STAIR(optLayID)
    if (layToAdd == 2 or layToAdd == 0):
        TEN_CIRC_LIFT(optLayID)
    if (layToAdd == 3 or layToAdd == 0):
        TEN_CIRC_ESCL(optLayID)
    return None

if __name__=="__main__":
    rs.EnableRedraw(False)
    main()
    rs.EnableRedraw(True)