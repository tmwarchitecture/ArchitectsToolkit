###Reads a csv file and adds layers based on it.
import rhinoscriptsyntax as rs

filename = "C:\Users\Tim\Desktop\Rhino Layers - Sheet1.csv"

def addLayerFromCSV(layerRow):
    #ROOT LAYER COLUMN 
    #(A=0, B=1, C=2)
    rootCol = 0
    opNumCol = 1
    catCol = 2
    elementCol = 3
    clrCol = 4
    matCol = 5
    lineTyCol = 6
    
    file = open(filename, "r")
    contents = file.readlines()
    file.close()
    
    layerData = []
    for content in contents:
        layerData.append(content.split(","))
    layerData = layerData[1:18] #trim first row
    
    rootLay = layerData[layerRow][rootCol]
    opNum = layerData[layerRow][opNumCol]
    catLay = layerData[layerRow][catCol]
    elementName = layerData[layerRow][elementCol]
    layClr = layerData[layerRow][clrCol]
    layMtrl = layerData[layerRow][matCol]
    layLType = layerData[layerRow][lineTyCol]
    
    rootID = rs.AddLayer(rootLay)
    parentID = rs.AddLayer(opNum, parent = rootID)
    catID = rs.AddLayer(catLay, parent = parentID)
    
    #rs.AddLayer(elementName, layClr, parent = catLay)
    return None

addLayerFromCSV(0)