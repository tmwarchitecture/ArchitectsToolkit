#REFERENCE

import rhinoscriptsyntax as rs
import TEN_OP as op

def TEN_REF_CAD(optLayID):
    #subLayName = "FLOR"
    #subLayColor = [125,125,255]
    layName = "CAD"
    layColor = [100,200,255]
    layMatIndex = -1
    printColor = [0,0,0]
    printWidth = .18
    
    #ADD SUB-LAYER
    #subLayID = rs.AddLayer(subLayName, subLayColor, parent = optLayID)
    
    #ADD OBJECT LAYER
    lay = rs.AddLayer(layName, layColor, parent = optLayID)
    
    #CHANGE CURRENT LAYER TO NEW LAYER
    rs.CurrentLayer(lay)
    
    #CHANGE LAYER MATERIAL
    #rs.LayerMaterialIndex(lay, layMatIndex)
    
    #CHANGE LAYER PRINT ATTRIBUTES
    rs.LayerPrintColor(lay, printColor)
    rs.LayerPrintWidth(lay, printWidth)
    
    return None
def TEN_REF_SK(optLayID):
    #subLayName = "FLOR"
    #subLayColor = [125,125,255]
    layName = "Sketch"
    layColor = [100,200,255]
    layMatIndex = -1
    printColor = [0,0,0]
    printWidth = .18
    
    #ADD SUB-LAYER
    #subLayID = rs.AddLayer(subLayName, subLayColor, parent = optLayID)
    
    #ADD OBJECT LAYER
    lay = rs.AddLayer(layName, layColor, parent = optLayID)
    
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
    
    #OPTION NUMBER
    #optNum = rs.GetInteger("Enter Option Number", number = 01)
    optNum = op.getCurOp()
    if optNum is None:
        return
    if (len(str(optNum))<2):
        optNum = "0" + str(optNum)
    optName = "OP_" + str(optNum)
    
    #ADD BASE LAYER
    baseLay = "70_REF"
    baseLayID = rs.AddLayer(baseLay, [50,50,50])
    
    #ADD OPTION LAYER
    #optLayID = rs.AddLayer(optName, [50,50,50], parent = baseLayID)
    
    #ADD EACH LAYER
    if (layToAdd == 1 or layToAdd == 0):
        TEN_REF_CAD(baseLayID)
    if (layToAdd == 2 or layToAdd == 0):
        TEN_REF_SK(baseLayID)
    return None

if __name__=="__main__":
    rs.EnableRedraw(False)
    main()
    rs.EnableRedraw(True)