import rhinoscriptsyntax as rs

def setFloorLevels(numFloors):
    """
    sets the floor levels in document data
    input: int: the number of floors
    returns: None
    """
    levelName = []
    levels = []
    
    for i in range(0,numFloors):
        levelName.append("L"+str(i+1))
    levelName.append("Roof")
    
    #if existing data, get
    for i in range(0,numFloors):
        if (rs.GetDocumentData("Levels",levelName[i]) is not None):
            levels.append(rs.GetDocumentData("Levels", levelName[i]))
        else:
            levels.append(None)
    if (rs.GetDocumentData("Levels",levelName[-1]) is not None):
        levels.append(rs.GetDocumentData("Levels", levelName[-1]))
    else:
        levels.append(None)
    rs.DeleteDocumentData("Levels")
    newLevels = []
    newLevels = rs.PropertyListBox(levelName, levels, "LEVELS", "Update the Levels below")
    
    for i in range(0,numFloors+1):
        rs.SetDocumentData("Levels", levelName[i], str(newLevels[i]))
    return None
def getFloorLevels():
    """
    get the levels from document data
    input: None
    returns: List of levels
    """
    numFloors = getNumFloors()
    levelName = []
    levels = []
    
    for i in range(0,numFloors):
        levelName.append("L"+str(i+1))
        levels.append(float(rs.GetDocumentData("Levels", levelName[i])))
    levelName.append("Roof")
    levels.append(float(rs.GetDocumentData("Levels", levelName[-1])))
    
    return levels
def setNumFloors():
    try:
        curNum = int(rs.GetDocumentData("NumLevels", "NumLevels"))
    except:
        curNum = 1
    a = rs.GetInteger("Number of Levels in the building",minimum = 1, number = curNum)
    rs.SetDocumentData("NumLevels", "NumLevels", str(a))
    return None
def getNumFloors():
    a = rs.GetDocumentData("NumLevels", "NumLevels")
    if a is None:
        return 1
    else:
        return int(a)

if __name__=="__main__":
    func = rs.GetInteger("")
    if func == 0:
        setNumFloors()
    if func == 1:
        b = getNumFloors()
        setFloorLevels(b)
    if func == 2:
        print getFloorLevels()
        #setFloorLevels(b)
