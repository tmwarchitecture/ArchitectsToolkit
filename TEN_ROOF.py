#AR_ROOF

import rhinoscriptsyntax as rs
import opUtil as op

def TEN_ROOF_ROOF(optLayID):
    subLayName = "Roof"
    subLayColor = [125,125,255]
    layName = "ROOF"
    layColor = [200,200,200]
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
def TEN_ROOF_FNSH(optLayID):
    subLayName = "Roof"
    subLayColor = [125,125,255]
    layName = "FNSH"
    layColor = [101,101,101]
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
        TEN_ROOF_ROOF(optLayID)
    if (layToAdd == 2 or layToAdd == 0):
        TEN_ROOF_FNSH(optLayID)
    return None

if __name__=="__main__":
    rs.EnableRedraw(False)
    main()
    rs.EnableRedraw(True)