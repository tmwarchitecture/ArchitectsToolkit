#AR_GENERAL

import rhinoscriptsyntax as rs
def TEN_GEN_BLOCKS(optLayID):
    subLayName = "General"
    subLayColor = [125,125,255]
    layName = "BLOCKS"
    layColor = [50,50,50]
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
    
    #OPTION NUMBER
    #optNum = rs.GetInteger("Enter Option Number", number = 01)
    #if optNum is None:
    #    return
    #if (len(str(optNum))<2):
    #    optNum = "0" + str(optNum)
    #optName = "OP_" + str(optNum)
    
    #ADD BASE LAYER
    baseLay = "00_GEN"
    baseLayID = rs.AddLayer(baseLay, [50,50,50])
    
    #ADD OPTION LAYER
    #optLayID = rs.AddLayer(optName, [50,50,50], parent = baseLayID)
    
    #ADD EACH LAYER
    if (layToAdd == 1 or layToAdd == 0):
        TEN_GEN_BLOCKS(baseLayID)
    return None

if __name__=="__main__":
    rs.EnableRedraw(False)
    main()
    rs.EnableRedraw(True)