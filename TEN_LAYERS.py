import rhinoscriptsyntax as rs
def getParentLayNumbers(num):
    allParentLayers = []
    numHund = num-num%100
    numTens = num-num%10
    
    
    
    if  num%10 != 0:
        allParentLayers.append(numTens)
    if  num%100 != 0:
        allParentLayers.append(numHund)
    
    allParentLayers.append(num)
    
    uniqueLayers = sorted(list(set(allParentLayers)))
    
    return uniqueLayers

def addLayerFromCSV(layNumList):
    """
    Adds a layer from a CSV file
    Input: int - list of Layer numbers, associated with CSV layer number
    Returns: None
    """
    rhinoLayerFilePath = "C:\\Users\\Tim\\Desktop\\temp\\RhinoLayersV3.csv"
    
    #Read the CSV
    file = open(rhinoLayerFilePath, "r")
    contents = file.readlines()
    file.close()
    
    #Variables
    RhinoLayerCol = 1
    ColorCol = 3
    found = False
    
    allLayerInfo = []
    
    #Find layer info
    for row in contents:
        rowParts = row.split(",")
        for item in layNumList:
            #if layNum matches the CSV:
            if row.split(",")[0]==str(item):  
                thisLayInfo = []
                nameCol = row.split(",")[RhinoLayerCol]
                if len(nameCol)<1:
                    break
                thisLayInfo.append(row.split(",")[RhinoLayerCol])
                LayColorRaw = row.split(",")[ColorCol]
                if len(LayColorRaw)>1:
                    LayColor = (int(LayColorRaw.split("-")[0]),int(LayColorRaw.split("-")[1]),int(LayColorRaw.split("-")[2]))
                else:
                    LayColor = (0,0,0)
                thisLayInfo.append(LayColor)
                allLayerInfo.append(thisLayInfo)
                found = True
                break
    if not found:
        return None
    
    #Add Layer
    
    parent = None
    for eachItem in allLayerInfo:
        parent = rs.AddLayer(eachItem[0], color = eachItem[1], parent = parent)
    
    return parent

def main():
    type = rs.GetInteger("Input Layer Number to add", number = 0)
    
    if type is None:
        return
    
    layerNumbers = []
    
    if (type%100 == 0):
        for i in range(type, type+100):
            layerNumbers.append(i)
    elif (type%10 == 0):
        for i in range(type, type+9):
            layerNumbers.append(i)
    else:
        layerNumbers.append(type)
    
    
    rs.EnableRedraw(False)
    
    
    for num in layerNumbers:
        allNumbers = getParentLayNumbers(num)
        print addLayerFromCSV(allNumbers)
    
    rs.EnableRedraw(True)


if( __name__ == "__main__" ):
    main()    