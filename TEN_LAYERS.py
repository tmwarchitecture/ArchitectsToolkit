import rhinoscriptsyntax as rs

def addLayerFromCSV(layNum):
    """
    Adds a layer from a CSV file
    Input: int - Layer number, associated with CSV layer number
    Returns: None
    """
    rhinoLayerFilePath = "C:\\Users\\Tim\\Desktop\\temp\\RhinoLayers.csv"
    
    #Read the CSV
    file = open(rhinoLayerFilePath, "r")
    contents = file.readlines()
    file.close()
    
    #Variables
    CategoryCol = 1
    RhinoLayerCol = 2
    ColorCol = 5
    found = False
    
    #Find layer info
    for row in contents:
        rowParts = row.split(",")
        if row.split(",")[0]==str(layNum):
            RhinoLayName = row.split(",")[RhinoLayerCol]
            CategoryName = row.split(",")[CategoryCol]
            LayColorRaw = row.split(",")[ColorCol]
            if len(LayColorRaw)>1:
                LayColor = (int(LayColorRaw.split("-")[0]),int(LayColorRaw.split("-")[1]),int(LayColorRaw.split("-")[2]))
            else:
                LayColor = (0,0,0)
            found = True
            break
    if not found:
        return
    
    #Add Layer
    
    root = rs.AddLayer(CategoryName)
    rs.AddLayer(RhinoLayName, color = LayColor, parent = root)
    
    print CategoryName + "::" + RhinoLayName + " - " + LayColorRaw

def main():
    type = rs.GetInteger("Input Layer Number to add", number = 0)
    if type is None:
        return
    
    layerNumbers = []
    if (type%100 == 0):
        for i in range(type, type+999):
            layerNumbers.append(i)
    elif (type%10 == 0):
        for i in range(type, type+9):
            layerNumbers.append(i)
    else:
        layerNumbers.append(type)
    
    
    rs.EnableRedraw(False)
    
    
    
    for num in layerNumbers:
        addLayerFromCSV(num)
    
    rs.EnableRedraw(True)


if( __name__ == "__main__" ):
    main()    