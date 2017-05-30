import rhinoscriptsyntax as rs
import random
#import scriptcontext as sc
#import Rhino

def randCol(delta):
    newCol = int(random.uniform(delta*.8, delta))
    negBool = random.randint(0,1)
    if (negBool):
        newCol = newCol*-1
    return newCol

def iterate():
    colDelta = 20
    origLayer = rs.GetLayer("Select Layer to Iterate")
    if origLayer is None:
        return
    
    shortName = origLayer.split("::")[-1]
    parentLay = rs.ParentLayer(origLayer)
    nameParts = shortName.split("_")
    if len(nameParts)>1:
        num = int(nameParts[1])+1
    else:
        num = 1
    if len(str(num))==1:
        newNum = "0"+str(num)
    else:
        newNum = str(num)
    newName = nameParts[0]+"_"+newNum
    lay1 = rs.CurrentLayer(origLayer)
    
    #MAterials
    matIndex = rs.LayerMaterialIndex(lay1)
    
    
    #New Color
    oldCol = rs.LayerColor(lay1)
    oldRed = rs.ColorRedValue(oldCol)
    oldGreen = rs.ColorGreenValue(oldCol)
    oldBlue = rs.ColorBlueValue(oldCol)
    
    newRed = oldRed + randCol(colDelta)
    if newRed>255:
        newRed = 255 - (newRed-255)
    if newRed<0:
        newRed = abs(newRed)
        
    newGreen = oldGreen + randCol(colDelta)
    if newGreen>255:
        newGreen = 255 - (newGreen-255)
    if newGreen<0:
        newGreen = abs(newGreen)
        
    newBlue = oldBlue + randCol(colDelta)
    if newBlue>255:
        newBlue = 255 - (newBlue-255)
    if newBlue<0:
        newBlue = abs(newBlue)
    newCol = (newBlue, newGreen, newBlue)
    newLay = rs.AddLayer(newName, color = newCol, parent = parentLay)
    #print nameParts
    #print newName
    finalLayer = rs.CurrentLayer(newLay)
    #sc.doc.Layers.CurrentLayer.RenderMaterialIndex = 3
    #c = sc.doc.Layers.CurrentLayer.RenderMaterialIndex
    #sc.doc.Layers.Modify(
    #Rhino.DocObjects.Tables.LayerTable.CurrentLayer.r
    #sc.doc.Views.Redraw()
    #b = sc.doc.Layers.CurrentLayer
    #print ""
    return

if __name__=="__main__":
    iterate()