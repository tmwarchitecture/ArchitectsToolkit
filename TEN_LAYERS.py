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
    rhinoLayerFilePath = "Q:\\Staff Postbox\\Tim Williams\\10 DESIGN LAYERS\\dev\\LAYERS\\RhinoLayersV3.csv"
    
    #Read the CSV
    file = open(rhinoLayerFilePath, "r")
    contents = file.readlines()
    file.close()
    
    #Variables
    RhinoLayerCol = 1
    ColorCol = 3
    MaterialCol = 4
    LinetypeCol = 5
    PrintColorCol = 6
    PrintWidthCol = 7
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
                
                
                #Linetype
                LinetypeRaw = row.split(",")[LinetypeCol]
                if len(LinetypeRaw)>1:
                    Linetype = LinetypeRaw
                else:
                    Linetype = "Continuous"
                
                #Layer Color
                LayColorRaw = row.split(",")[ColorCol]
                if len(LayColorRaw)>1:
                    LayColor = (int(LayColorRaw.split("-")[0]),int(LayColorRaw.split("-")[1]),int(LayColorRaw.split("-")[2]))
                else:
                    LayColor = (0,0,0)
                
                #Print Color
                PrintColorRaw = row.split(",")[PrintColorCol]
                if len(PrintColorRaw)>1:
                    PrintColor = (int(PrintColorRaw.split("-")[0]),int(PrintColorRaw.split("-")[1]),int(PrintColorRaw.split("-")[2]))
                else:
                    PrintColor = (0,0,0)
                
                #Print Width
                PrintWidthRaw = row.split(",")[PrintWidthCol]
                if len(PrintWidthRaw)>1:
                    PrintWidth = float(PrintWidthRaw)
                else:
                    PrintWidth = float(0)
                
                thisLayInfo.append(LayColor)
                thisLayInfo.append(PrintColor)
                thisLayInfo.append(Linetype)
                thisLayInfo.append(PrintWidth)
                allLayerInfo.append(thisLayInfo)
                found = True
                break
    if not found:
        return None
    
    #Find root layer
    root = rs.LayerName(rs.CurrentLayer()).split("::")[0]
    #print root
    
    #Add Layer
    parent = None
    for eachItem in allLayerInfo:
        parent = rs.AddLayer(eachItem[0], color = eachItem[1], parent = parent)
        rs.LayerPrintColor(parent, eachItem[2])
        rs.LayerLinetype(parent, eachItem[3])
        rs.LayerPrintWidth(parent, eachItem[4])
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
        addLayerFromCSV(allNumbers)
    
    rs.EnableRedraw(True)


if( __name__ == "__main__" ):
    main()    
