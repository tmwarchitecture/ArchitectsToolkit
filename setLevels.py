import rhinoscriptsyntax as rs

def setFloorLevels(numFloors):
    """
    sets the floor levels in document data
    input: int: the number of floors
    returns: None
    """
    levelNum = []
    levels = []
    
    for i in range(0,numFloors):
        levelNum.append("L"+str(i+1))
    
    #if existing data, get
    for i in range(0,numFloors):
        if (rs.GetDocumentData("Levels",levelNum[i]) is not None):
            levels.append(rs.GetDocumentData("Levels", levelNum[i]))
        else:
            levels.append(None)
    rs.DeleteDocumentData("Levels")
    newLevels = []
    newLevels = rs.PropertyListBox(levelNum, levels, "LEVELS", "Update the Levels below")
    
    for i in range(0,numFloors):
        rs.SetDocumentData("Levels", levelNum[i], str(newLevels[i]))
    return None
def getFloorLevels():
    """
    get the levels from document data
    input: None
    returns: List of levels
    """
    numFloors = getNumFloors()
    levelNum = []
    levels = []
    
    for i in range(0,numFloors):
        levelNum.append("L"+str(i+1))
        levels.append(float(rs.GetDocumentData("Levels", levelNum[i])))
    
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
