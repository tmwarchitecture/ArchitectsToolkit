import rhinoscriptsyntax as rs
import Rhino
import datetime
def diff(list1, list2):
    c = set(list1).union(set(list2))
    d = set(list1).intersection(set(list2))
    return list(c - d)
def exportTEN_CAD():
    a = rs.GetObjects("Select Objects", preselect = "True")
    b = rs.ScaleObjects(a, [0,0,0], [1000,1000,0], copy=True)
    rs.UnitSystem(2)
    
    savePath0 = rs.SaveFileName("Save", "Autocad (*.dwg)|*.dwg||")
    savePath1 = '"'+savePath0+'"'
    rs.SelectObjects(b)
    rs.Command('_-Export '+savePath1+' _Enter')
    rs.DeleteObjects(b)
    rs.UnitSystem(4)
    print "Exported"
    return None
def exportPlanToCAD(chosenLevel, path):
    
    #Make sure layer is visible
    rs.LayerVisible("6_DRAWINGS", True)
    chosenChildren = rs.LayerChildren("6_DRAWINGS::"+chosenLevel)
    objects = []
    for chosenChild in chosenChildren:
        tempObjects = rs.ObjectsByLayer(chosenChild)
        for tempObject in tempObjects:
            objects.append(tempObject)
    if objects is None:
        return
    
    scaledObjects = rs.ScaleObjects(objects, [0,0,0], [1000,1000,0], copy=True)
    
    #Format Coordinate
    #    rawCoordinate = rs.GetDocumentData("Project Info", "CAD coordinate")
    #    coordinate = rawCoordinate.split(",")
    #    try:
    #        for i in range(0, 3):
    #            coordinate[i] = float(coordinate[i])
    #    except:
    #            coordinate = None
    #    if coordinate is None:
    #        print "CAD coordinate has an error"
    #    
    #    else: #move all objects
    #        negVec = rs.VectorReverse(coordinate)
    #        rs.MoveObjects(scaledObjects, coordinate)
    
    
    rs.UnitSystem(2)
    
    savePath1 = '"'+path+'"'
    rs.SelectObjects(scaledObjects)
    rs.Command('_-Export '+savePath1+' _Enter')
    rs.DeleteObjects(scaledObjects)
    rs.UnitSystem(4)
    print "Exported"
    return None
def exportAllPlansToCAD():
    if rs.IsLayer("6_DRAWINGS"):
        children = rs.LayerChildren("6_DRAWINGS")
        items = []
        for child in children:
            items.append(rs.LayerName(child, False))
        #level = rs.ComboListBox(items)
        print rs.DocumentPath()
        pathParts = rs.DocumentPath().split("\\")
        if pathParts[0] == "P:":
            defaultPath = pathParts[0] +"\\" + pathParts[1] +"\\" + pathParts[2] +"\\" + pathParts[3]
            folder = rs.BrowseForFolder(folder = defaultPath, message = "Select Folder to export plans.", title = "Export Plans")
        else:
            folder = rs.BrowseForFolder()
        RhinoFile = rs.DocumentName()
        rhinoName = RhinoFile.split(".")[0] + "_P_"
        
        for item in items:
            levelNum = item.split("_")[-1]
            fileName = "\\" + rhinoName + levelNum + ".dwg"
            savePath = folder + fileName
            #savePath = rs.SaveFileName("Save", "Autocad (*.dwg)|*.dwg||")
            if savePath is not None:
                exportPlanToCAD(item, savePath)
    else:
        print "No plans currently cut. Use CutPlans."
    return
def importTEN_CAD():
    savePath0 = rs.OpenFileName("Open", "Autocad (*.dwg)|*.dwg||")
    items = [ ["Units", "Meters", "Millimeters"] ]
    defaults = [False]
    CADinMilli = rs.GetBoolean("Is that CAD file in meters or mm?", items, defaults)[0]
    
    explodeBlockBoo = True
    
    if savePath0 is None:
        return
    rs.EnableRedraw(False)
    
    #setup the layers
    rs.AddLayer("7_REF")
    rs.AddLayer("CAD", parent = "7_REF")
    
    fileNameExt = savePath0.split('\\')[-1]
    fileName = fileNameExt.split('.')[0]
    savePath1 = '"'+savePath0+'"'
    
    #create layer name
    now = datetime.date.today()
    dateList = []
    if len(str(now.month))>1:
        month = str(now.month)
    else:
        month = "0"+str(now.month)
    if len(str(now.day))>1:
        day = str(now.day)
    else:
        day = "0"+str(now.day)
    time = str(now.year)+month+day
    layerName = time+"_"+fileName+"_01"
    children = rs.LayerChildren("7_REF::CAD")
    finalNums = []
    for child in children:
        num = rs.LayerName(child, fullpath = False).split("_")[-1]
        try:
            finalNums.append(int(num))
        except:
            finalNums.append(0)
    finalNums.sort()
    if rs.IsLayer("7_REF::CAD::"+layerName):
        num = int(finalNums[-1])+1
        if len(str(num))<2:
            finalNum = "0" + str(num)
        else:
            finalNum = str(num)
        layerName = time+"_"+fileName+ "_" + finalNum
    par = rs.AddLayer("7_REF")
    cat = rs.AddLayer("CAD", parent = par)
    element = rs.AddLayer(layerName, parent = cat)
    rs.CurrentLayer(element)
    
    #get intial list of all layers in the file
    currentLayers = rs.LayerNames()
    
    rs.Command('_-Import '+savePath1+' _Enter')
    
    #get new layers added
    endLayersNames = rs.LayerNames()
    #newLayers = [item for item in currentLayers if item not in endLayersNames]
    newLayers = diff(endLayersNames, currentLayers)
    print newLayers
    
    
    
    
    for layer in newLayers:
        rs.ParentLayer(layer, element)
        objects = rs.ObjectsByLayer(layer)
        if rs.IsLayerEmpty(layer):
            rs.DeleteLayer(layer)
        else:
            for obj in objects:
                if rs.IsDimension(obj):
                    rs.DeleteObject(obj)
                elif rs.IsHatch(obj):
                    rs.DeleteObject(obj)
    
    #Get all the imported geometry
    allObjects = []
    finalLayers = rs.LayerChildren(rs.CurrentLayer())
    for finalLayer in finalLayers:
        allObjects.append(rs.ObjectsByLayer(finalLayer))
    finalAllObjects = [item for sublist in allObjects for item in sublist]
    
    #Format Coordinate
    try:
        rawCoordinate = rs.GetDocumentData("Project Info", "CAD coordinate (X,Y,Z)")
    except:
        print "No CAD Coordinate specified in the Project Info"
        rawCoordinate = (0,0,0)
    coordinate = rawCoordinate.split(",")
    print "Aa"
    
    try:
        for i in range(0, 3):
            coordinate[i] = float(coordinate[i])
    except:
            coordinate = None
    if coordinate is None:
        print "CAD coordinate has an error"
    
    else: #move all objects
        negVec = rs.VectorReverse(coordinate)
        rs.MoveObjects(finalAllObjects, negVec)
    
    if CADinMilli:
        rs.ScaleObjects(finalAllObjects, [0,0,0], [.001, .001, .001])
    
    importGroup = rs.AddGroup(str(layerName))
    
    rs.AddObjectsToGroup(finalAllObjects, importGroup)
    
    rs.ZoomSelected()
    print "Import EXECUTED"
    rs.EnableRedraw(True)
    return None

if __name__=="__main__":
    type = rs.GetInteger("", number = 0)
    if (type == 0):
        exportTEN_CAD()
    elif (type == 1):
        #Import CAD
        importTEN_CAD()
    elif (type == 2):
        #Export All plans
        if rs.IsLayer("6_DRAWINGS"):
            children = rs.LayerChildren("6_DRAWINGS")
            items = []
            for child in children:
                items.append(rs.LayerName(child, False))
            level = rs.ComboListBox(items)
            print rs.DocumentPath()
            pathParts = rs.DocumentPath().split("\\")
            if pathParts[0] == "P:":
                defaultPath = pathParts[0] +"\\" + pathParts[1] +"\\" + pathParts[2] +"\\" + pathParts[3]
                folder = rs.BrowseForFolder(folder = defaultPath, message = "Select Folder to export plan.", title = "Export Plan")
            else:
                folder = rs.BrowseForFolder()
            RhinoFile = rs.DocumentName()
            rhinoName = RhinoFile.split(".")[0] + "_P_"
            levelNum = level.split("_")[-1]
            fileName = "\\" + rhinoName + levelNum + ".dwg"
            savePath = folder + fileName
            #savePath = rs.SaveFileName("Save", "Autocad (*.dwg)|*.dwg||")
            if savePath is not None:
                exportPlanToCAD(level, savePath)
        else:
            print "No plans currently cut. Use CutPlans."
    elif (type == 3):
        exportAllPlansToCAD()
